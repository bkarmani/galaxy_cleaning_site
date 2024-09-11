from . import main
from flask import render_template


@main.route('/index')
@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/about')
def about_page():
    return render_template('about.html')


@main.route('/services')
def services_page():
    return render_template('services.html')


@main.route('/services/details')
def services_details():
    return render_template('service-details.html')


@main.route('/blog')
def blog_page():
    return render_template('blog.html')


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


@main.route('/team')
def team():
    return render_template('team.html')


@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')
