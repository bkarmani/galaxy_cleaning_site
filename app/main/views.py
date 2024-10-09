from . import main
from flask import render_template, request, current_app, redirect, flash, abort, url_for
from app.models import Projects, Post, Subscribers
from .forms import QuotesForm
import os,re
from app import db
from itsdangerous import URLSafeSerializer, BadSignature


# @main.app_context_processor
# def inject_api():
#     return dict(google_maps_api_key="AIzaSyCUoE5ByYXVku3UhXqwf_XO_lY0-FnCjb4")
# Global variable to track the total projects done



# Function to increment the project count
# def increment_projects_done():
#     with app.app_context():
#         old_record = Projects.query.first()
#         if old_record:
#             old_record.number_of_projects += 1
#             db.session.commit()
#     print(f"Total projects done: {old_record}")

# # Initialize the scheduler outside the route so it's not initialized on every request
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=increment_projects_done, trigger="interval", minutes=1)  # Run every minute
# scheduler.start()

# Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())

s = URLSafeSerializer('kjhcdgucbgudxusdyytctcdxyv')

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@main.app_template_filter('truncate_body')
def truncate_body(text, num_words=20):
    words = text.split()
    if len(words) > num_words:
        return ' '.join(words[:num_words]) + '...'
    return text


@main.route('/index', methods=['GET', 'POST'])
@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def index():
    form = QuotesForm()
    record = Projects.query.first()
    projects = record.total_projects

    posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    hashed_posts = [
        {"token": s.dumps(post.id), "post": post} for post in posts
    ]
    if form.validate_on_submit():
        form_data = {
            'name':form.name.data,
            'email' : form.email.data,
            'phone_num' : form.phone.data,
            'address' : form.address.data,
            'comments' : form.comments.data,
            'selected_service' : form.cleaning_service,
            'date' : form.date.data,
            'time' : form.time.data,
            'zipcode' : form.zip_code.data,
            'budget' : form.budget.data,
            'approx_sf' : form.approx_sf.data,
            'property_type' : form.property_type.data
        }
        # send email algor

        # notify user of success
        flash(f"Thank you! {form_data['name']}, we'll get back to you shortly", category='success')
        return redirect(url_for('main.index'))

    return render_template('index.html', total_projects=projects, recent_posts=hashed_posts, form=form)


@main.route('/about')
def about_page():
    return render_template('about1.html')


@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe_user():
    if request.method == 'POST':
        email = request.form.get('sub_email')
        is_a_subscriber = Subscribers.query.filter_by(email=email).first()
        if is_a_subscriber:
            flash('sorry!, you are already a subscriber', category='warning')
            # print('sorry!, you are already a subscriber')
        elif email=='':
            flash('this field cannot be empty', category='error')
            # print('this field cannot be empty')
        elif not is_valid_email(email):
            flash('please enter a valid email', category='warning')
            # print('please enter a valid email')
        else:
            user = Subscribers(email=email)
            db.session.add(user)
            db.session.commit()
            # print('you have subscribed successfully')
            # subscribe_user(email, 
            #             'electron@sandboxa7f55fb25a5444a0addd0fc153c3039c.mailgun.org',
            #             '8023f9a76db2402179a28cb1bbd8a16b-4e034d9e-3058ef0c')
            flash('you have successfully subscribed to our newsletter', category='success')
            # subject='NEWSLETTER SUBSCRIPTION'
            # sender= admin_sender
            # recipient = email
            # template = 'emails/newsletter'
            # send_email(subject,sender, recipient, template, user=email)
    return redirect(request.referrer)

# list all services in a page
@main.route('/services')
def services_page():
    return render_template('service1.html')

# --- list of services offered starts here ---

# residential cleaning service

@main.route('/service/residential-cleaning')
def residential():
    return render_template('residential.html')

# commercial cleaning service
@main.route('/service/commercial-cleaning')
def commercial():
    return render_template('commercial.html')

# car wash cleaning service
@main.route('/service/car-wash')
def car_wash():
    return render_template('car-wash.html')

# custom cleaning service tailored to your request/needs
@main.route('/service/custom-cleaning')
def custom_clean():
    return render_template('custom-clean.html')

# green cleaning service
@main.route('/service/green-cleaning')
def green_clean():
    return render_template('green-clean.html')

# sanitized cleaning services 
@main.route('/service/sanitization-cleaning')
def sanitize():
    return render_template('sanitization.html')

@main.route('/service/specialized-cleaning')
def specialized():
    return render_template('specialized.html')

# -- end of all services --



# @main.route('/team/members')
# def teams_page():
#     return render_template('team1.html')

# @main.route('/team/members/<int:num>')
# def team1(num):
#     return render_template('single-team1.html', num=num)

# @main.route('/team/members/<int:num>')
# def team2(num):
#     return render_template('single-team2.html', num=num)

# @main.route('/team/members/<int:num>')
# def team3(num):
    return render_template('single-team3.html', num=num)

@main.route('/blog/', methods=['GET', 'POST'])
def blog_page():
    # Get the search query from the request
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)

    # Filter posts based on the search query if provided
    if query:
        pagination = Post.query.filter(Post.title.ilike(f'%{query}%')).order_by(Post.timestamp.desc()).paginate(
            page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False
        )
    else:
        # If no query, just get the latest posts
        pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
            page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False
        )

    
    hashed_posts=[
        {"token": s.dumps(post.id), "post": post} for post in pagination.items
    ]
    recent_posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    hashed_recent_posts = [
        {"token": s.dumps(post.id), "post": post} for post in recent_posts
    ]
    return render_template('blog2.html', pagination=pagination, recent_posts=hashed_recent_posts, query=query, hashed_posts=hashed_posts)


@main.route('/blog/<string:token>')
def blog_detail(token):
    recent_posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    hashed_recent_posts = [
        {"token": s.dumps(post.id), "post": post} for post in recent_posts
    ]
    try:  
        post_id = s.loads(token)        
        post = Post.query.get_or_404(post_id)
    except BadSignature:
        abort(404)
    return render_template('single-blog1.html', post=post, recent_posts=hashed_recent_posts)


@main.route('/projects/')
def projects_page():
    recent_projects = Projects.query.order_by(Projects.id.desc()).limit(6).all()
    hashed_projects = [
        {"token": s.dumps(project.id), "project": project} for project in recent_projects
    ]
    return render_template('project1.html', projects=hashed_projects)



@main.route('/projects/<string:token>')
def project_detail(token):
    recent_posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    hashed_recent_posts = [
        {"token": s.dumps(post.id), "post": post} for post in recent_posts
    ]
    try:  
        projects_id = s.loads(token)        
        project = Projects.query.get_or_404(projects_id)
    except BadSignature:
        abort(404)
    return render_template('single-project1.html', project=project, recent_posts=hashed_recent_posts)


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/message-us', methods=['GET', 'POST'])
def message_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        flash('thank you for messaging us, we will get back to you shortly', category='success')
        # send email algo goes here
    return redirect(request.referrer)


@main.route('/services/service_details')
def service_details():
    return render_template('service-details.html')


@main.route('/team')
def team():
    return render_template('team.html')


@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


@main.route('/privacy')
def privacy():
    return render_template('privacy.html')


@main.route('/terms')
def terms_of_service():
    return render_template('terms.html')


@main.route('/request-estimate', methods=['GET', 'POST'])
def request_estimate():
    form = QuotesForm()
    if form.validate_on_submit():
        flash('success, we shall get back to you shortly', category='success')
        return redirect(url_for('main.index'))
    return render_template('calculate-form.html', form=form)


@main.route('/get-estimate', methods=['GET', 'POST'])
def get_estimate():
    if request.method == 'POST':
        name = request.form.get('email')
                
    return redirect(request.referrer)

