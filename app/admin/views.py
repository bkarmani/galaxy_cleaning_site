from flask import url_for, redirect, render_template, flash, current_app
from . import admin
from .forms import BlogPostForm
from ..models import Post
from app import db
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename


@admin.route('//')
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

