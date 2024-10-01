from . import main
from flask import render_template, request, current_app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.models import Projects, Post
import os
from app import db


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

@main.route('/index')
@main.route('/')
@main.route('/home')
def index():
    record = Projects.query.first()
    total_projects = record.number_of_projects

    return render_template('index.html', total_projects=total_projects)

@main.route('/about')
def about_page():
    return render_template('about1.html')

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



@main.route('/team/members')
def teams_page():
    return render_template('team1.html')

@main.route('/team/members/<int:num>')
def team1(num):
    return render_template('single-team1.html', num=num)

@main.route('/team/members/<int:num>')
def team2(num):
    return render_template('single-team2.html', num=num)

@main.route('/team/members/<int:num>')
def team3(num):
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

    posts = pagination.items
    recent_posts = Post.query.order_by(Post.timestamp.desc()).limit(3).all()
    return render_template('blog2.html', posts=posts, pagination=pagination, recent_posts=recent_posts, query=query)


@main.route('/projects')
def projects_page():
    return render_template('project1.html')


@main.route('/blog/detail')
def blog_detail():
    return render_template('blog-details.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/services/digital-marketing')
def digital_marketing():
    return render_template('digital-marketing.html')


@main.route('/services/ui-ux-design')
def ui_ux_design():
    return render_template('ui-ux-design.html')


@main.route('/services/seo-marketing')
def seo_marketing():
    return render_template('seo-marketing.html')


@main.route('/services/graphic-design')
def graphic_design():
    return render_template('graphic-design.html')


@main.route('/services/development')
def web_dev():
    return render_template('web-development.html')


@main.route('/services/service_details')
def service_details():
    return render_template('service-details.html')

@main.route('/book_service')
def book_service():
    return render_template('calculate-form.html')


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

