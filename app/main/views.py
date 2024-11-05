from . import main
from flask import render_template,render_template_string,send_from_directory, request, current_app, redirect, flash, abort, url_for, Response
from app.models import Projects, Post, Subscribers, TeamMember
from .forms import QuotesForm
import os,re
from app import db
from itsdangerous import URLSafeSerializer, BadSignature
from ..emails import send_email, send_message_us





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

@main.route('/sitemap.xml', methods=['GET'])
def sitemap():
    urls = [
        {'loc': url_for('main.index',_external=True)},
        {'loc': url_for('main.about_page',_external=True)},
        {'loc': url_for('main.services_page',_external=True)},
        {'loc': url_for('main.residential',_external=True)},
        {'loc': url_for('main.commercial',_external=True)},
        {'loc': url_for('main.car_wash',_external=True)},
        {'loc': url_for('main.custom_clean',_external=True)},
        {'loc': url_for('main.green_clean',_external=True)},
        {'loc': url_for('main.sanitize',_external=True)},
        {'loc': url_for('main.specialized',_external=True)},
        {'loc': url_for('main.recruitment',_external=True)},
        {'loc': url_for('main.blog_page',_external=True)},
        {'loc': url_for('main.blog_detail', token='',_external=True)},
        {'loc': url_for('main.projects_page',_external=True)},
        {'loc': url_for('main.project_detail',token='',_external=True)},
        {'loc': url_for('main.contact',_external=True)},
        {'loc': url_for('main.privacy',_external=True)},
        {'loc': url_for('main.terms_of_service',_external=True)}
        # ... other URLs
    ]
    sitemap_xml = render_template_string(
        """<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            {% for url in urls %}
            <url>
                <loc>{{ url['loc']|safe }}</loc>
            </url>
            {% endfor %}
        </urlset>
        """,
        urls=urls
    )
    return Response(sitemap_xml, mimetype='application/xml')

@main.route('/robots.txt')
def robots_txt():
    return send_from_directory(current_app.static_folder, 'robots.txt')



@main.route('/index', methods=['GET', 'POST'])
@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def index():
    form = QuotesForm()
    record = Projects.query.first()
    # projects = record.total_projects

    posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    hashed_posts = [
        {"token": s.dumps(post.id), "post": post} for post in posts
    ]
    if request.method == 'POST':
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
                'pet_count': form.pet_count.data,
                'budget' : form.budget.data,
                'approx_sf' : form.approx_sf.data
            }
            # send email to owner
            subject = 'Quotes Confirmation'
            recipient = form_data['email']
            owner = os.getenv('MY_EMAIL')
            sender = os.getenv('MY_EMAIL')
            owner_template = 'emails/notify-owner'
            customer_template = 'emails/customer-quote-confirmation'
            #send notification email to owner
            try:
                send_email(
                    subject,
                    sender, 
                    owner, 
                    owner_template, 
                    email=form_data['email'], 
                    customer_name=form_data['name'],  
                    phone_number=form_data['phone_num'], 
                    comments=form_data['comments'],
                    address=form_data['address'],
                    chosen_service=form_data['selected_service'],
                    date=form_data['date'],
                    time=form_data['time'],
                    zipcode=form_data['zipcode'],
                    pets=form_data['pet_count'],
                    budget=form_data['budget'],
                    property_size=form_data['approx_sf']
                )
            except Exception as err:
                print(f'{err}: quotes could not be sent at the moment')
            # send notification email to user
            try:
                send_email(
                    subject,
                    sender, 
                    recipient, 
                    customer_template,
                    customer_name=form_data['name']
                )
            except Exception as e:
                print(e)
                
            # notify user of success
            flash(f"Thank you! {form_data['name']}, we'll get back to you shortly", category='success')
            return redirect(url_for('main.index'))
        else:
            flash('Please correct the errors below and try again.', category='error')

    return render_template('index.html', recent_posts=hashed_posts, form=form)


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

        # notify customer via email 
            display_name = 'galaxy cleaning'
            send= os.getenv('MY_EMAIL')
            sender = f'{display_name} <{send}>'
            recipient = email
            subject='NEWSLETTER SUBSCRIPTION'
            template = 'emails/newsletter'
            
            send_email(subject,sender, recipient, template, email=email)
            flash('you have successfully subscribed to our newsletter', category='success')   
    return redirect(request.referrer)


@main.route('/unsubscribe/<email>')
def unsubscribe(email):
    mail = Subscribers.query.filter_by(email=email).first()
    if not mail:
        flash('you are no longer a subscriber', category='info')
    else:
        db.session.delete(mail)
        db.session.commit()
        flash('you have sucessfully unsubscribed from our newsletter', category='success')
    return redirect(url_for('main.index'))
 

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

@main.route('/service/recruitment')
def recruitment():
    return render_template('recruitment.html')

# -- end of all services --



@main.route('/team/', methods=['GET', 'POST'])
def teams_page():
    # Get the search query from the request
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)

    # Filter posts based on the search query if provided
    if query:
        pagination = TeamMember.query.filter(TeamMember.first_name.ilike(f'%{query}%')).order_by(TeamMember.id.desc()).paginate(
            page=page, per_page=current_app.config['FLASKY_TEAM_PER_PAGE'], error_out=False
        )
    else:
        # If no query, just get the latest posts
        pagination = TeamMember.query.order_by(TeamMember.id.desc()).paginate(
            page=page, per_page=current_app.config['FLASKY_TEAM_PER_PAGE'], error_out=False
        )

    
    hashed_team=[
        {"token": s.dumps(team.id), "team": team} for team in pagination.items
    ]
    return render_template('team1.html', pagination=pagination, teams=hashed_team, query=query)

@main.route('/team/<string:token>')
def team_detail(token): 
    teams = TeamMember.query.order_by(TeamMember.id.desc()).all()
    hashed_team = [
        {"token": s.dumps(team.id), "team": team} for team in teams
    ]
    try:  
        team_id = s.loads(token)        
        team = TeamMember.query.get_or_404(team_id)
    except BadSignature:
        abort(404)
    return render_template('single-team1.html', hashed_team_members=hashed_team, team=team )


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

        mail_subject = subject
        sender = os.getenv('MY_EMAIL')
        recipient = email
        user_template = 'emails/message-us'
        comment = message

        # Call the function to send the message with reply_to set to the user's email
        send_message_us(
            mail_subject,
            sender,
            recipient,
            user_template,
            msg=comment,
            customer_name=name,
            customer_phone=phone
        )

        flash('Thank you for messaging us, we will get back to you shortly', category='success')
    return redirect(request.referrer)


# @main.route('/services/service_details')
# def service_details():
    return render_template('service-details.html')


# @main.route('/team')
# def team():
#     return render_template('team.html')



@main.route('/privacy')
def privacy():
    return render_template('privacy.html')


@main.route('/terms')
def terms_of_service():
    return render_template('terms.html')


@main.route('/request-estimate', methods=['GET', 'POST'])
def request_estimate():
    form = QuotesForm()
    if request.method == 'POST':
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
                'pet_count': form.pet_count.data,
                'budget' : form.budget.data,
                'approx_sf' : form.approx_sf.data
            }
            # send email to owner
            subject = 'Quotes Confirmation'
            recipient = form_data['email']
            owner = os.getenv('MY_EMAIL')
            send_as = 'Galaxy Cleaning'
            sendr = os.getenv('MY_EMAIL')
            sender =f'{send_as} <{sendr}>'
            owner_template = 'emails/notify-owner'
            customer_template = 'emails/customer-quote-confirmation'
            #send notification email to owner
            try:
                send_email(
                    subject,
                    sender, 
                    owner, 
                    owner_template, 
                    email=form_data['email'], 
                    customer_name=form_data['name'],  
                    phone_number=form_data['phone_num'], 
                    comments=form_data['comments'],
                    address=form_data['address'],
                    chosen_service=form_data['selected_service'],
                    date=form_data['date'],
                    time=form_data['time'],
                    zipcode=form_data['zipcode'],
                    pets=form_data['pet_count'],
                    budget=form_data['budget'],
                    property_size=form_data['approx_sf']
                )
            except Exception as err:
                print(f'{err}: quotes could not be sent at the moment')
            # send notification email to user
            try:
                send_email(
                    subject,
                    sender, 
                    recipient, 
                    customer_template,
                    customer_name=form_data['name']
                )
            except Exception as e:
                print(e)
                
            # notify user of success
            flash(f"Thank you! {form_data['name']}, we'll get back to you shortly", category='success')
            return redirect(url_for('main.index'))
        else:
            flash('Please correct the errors below and try again.', category='error')
    return render_template('calculate-form.html', form=form)


@main.route('/get-estimate', methods=['GET', 'POST'])
def get_estimate():
    if request.method == 'POST':
        name = request.form.get('email')
                
    return redirect(request.referrer)

