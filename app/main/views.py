from . import main
from flask import render_template


@main.app_context_processor
def inject_api():
    return dict(google_maps_api_key="AIzaSyCUoE5ByYXVku3UhXqwf_XO_lY0-FnCjb4")


@main.route('/index')
@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/about')
def about_page():
    return render_template('about1.html')


@main.route('/services')
def services_page():
    return render_template('service1.html')


# @main.route('/services/details/<string:service>')
# def services_details1(service):
#     return render_template('single-service1.html', service=service)

# @main.route('/services/details/<string:service>')
# def services_details2(service):
#     return render_template('single-service2.html', service=service)

# @main.route('/services/details/<string:service>')
# def services_details3(service):
#     return render_template('single-service3.html', service=service)

@main.route('/services/details/residential-cleaning')
def residential():
    return render_template('residential.html')

@main.route('/services/details/commercial-cleaning')
def commercial():
    return render_template('commercial.html')

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

@main.route('/blog')
def blog_page():
    return render_template('blog2.html')

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


@main.route('/team')
def team():
    return render_template('team.html')


@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')
