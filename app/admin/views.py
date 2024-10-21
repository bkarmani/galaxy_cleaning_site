from flask import url_for, redirect, render_template, flash, current_app
from . import admin
from .forms import BlogPostForm, ProjectForm
from ..models import Post, Projects
from app import db
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename


@admin.route('/')
@login_required
def dashboard():
    form = BlogPostForm()
    if form.validate_on_submit():
        # Process the form data
        title = form.title.data
        body = form.body.data
        post = Post(
            title = title,
            body = body
        )
        db.session.add(post)
        db.session.commit()
        
        # Save the data (e.g., to the database)
        # Implement your logic to save the post here

        flash('Post created successfully!', 'success')
    return render_template('admin/dashboard.html', form=form)




@admin.route('/postblog', methods=['GET', 'POST'])
@login_required
def post_blog():
    form = BlogPostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        event_date = form.time.data
        
        # Ensure the upload folder exists
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])

        # Handle image upload
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)  # Secure the filename
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)  # Construct the full path
            
            # Save the image to the specified directory
            image_file.save(image_path)
        post = Post(
            title=title,
            body = body,
            timestamp = event_date,
            image_url=image_filename,
            author = current_user
        )
        db.session.add(post)
        db.session.commit()

        # Here you would typically save the post to the database
        # For example: save_post_to_db(title, body, event_date, image_filename)

        flash('Post created successfully!', 'success')
        return redirect(url_for('admin.post_blog'))
    return render_template('admin/post/post.html', form=form)

@admin.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/post/posts.html', posts=posts)




@admin.route('/create-projects', methods=['GET', 'POST'])
@login_required
def create_projects():
    form = ProjectForm()
    if form.validate_on_submit():
        title = form.title.data
        intro = form.introduction.data
        category = form.category.data
        client = form.client.data
        start = form.start.data
        ended = form.ended.data
        execution_title = form.execution_title.data
        execution_body = form.execution_body.data
        problems_title = form.problems_title.data
        problems_body = form.problems_body.data
        solutions_title = form.solutions_title.data
        solutions_body = form.solutions_body.data
        total_projects = form.total_projects.data
        
        # Ensure the upload folder exists
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])

        # Handle image upload
        if form.image1.data or form.image2.data:
            image1_file = form.image1.data
            image2_file = form.image2.data
            image1_filename = secure_filename(image1_file.filename)  # Secure the filename
            image2_filename = secure_filename(image2_file.filename)
            image1_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image1_filename)  # Construct the full path
            image2_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image2_filename)
            
            # Save the image to the specified directory
            image1_file.save(image1_path)
            image2_file.save(image2_path)

        projects = Projects(
            title=title,
            introduction = intro,
            category = category,
            client=client,
            start = start,
            ended = ended,
            execution_title = execution_title,
            execution_body = execution_body,
            problems_title = problems_title,
            problems_body = problems_body,
            solutions_title = solutions_title,
            solutions_body = solutions_body,
            image1_url = image1_filename,
            image2_url =image2_filename,
            total_projects = total_projects
        )
        db.session.add(projects)
        db.session.commit()

        # Here you would typically save the post to the database
        # For example: save_post_to_db(title, body, event_date, image_filename)

        flash('Post created successfully!', 'success')
        return redirect(url_for('admin.create_projects'))
    return render_template('admin/post/post-project.html', form=form)









