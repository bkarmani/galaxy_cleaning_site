from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
import datetime
from flask_wtf.file import FileAllowed

class BlogPostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'gif'], 'Images only!')])
    time = DateTimeField('Event Date',
                         format='%Y-%m-%d %H:%M',
                         validators=[DataRequired()],
                         default=datetime.datetime.now)
    submit = SubmitField('Submit Post')


class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    introduction = CKEditorField('Intro Body', validators=[DataRequired()])
    category = StringField('Project Category', validators=[DataRequired()])
    client = StringField('Project Client', validators=[DataRequired()])
    start = DateTimeField('Project Start Date',
                         format='%Y-%m-%d %H:%M',
                         validators=[DataRequired()])
    ended = DateTimeField('Project End Date',
                         format='%Y-%m-%d %H:%M',
                         validators=[DataRequired()])
    execution_title = StringField('Execution Title', validators=[DataRequired()])
    execution_body = CKEditorField('Execution Body', validators=[DataRequired()])
    problems_title = StringField('Problem Title', validators=[DataRequired()])
    problems_body = CKEditorField('Problem Body', validators=[DataRequired()])
    solutions_title = StringField('Solution Title', validators=[DataRequired()])
    solutions_body = CKEditorField('Solution Body', validators=[DataRequired()])
    total_projects = IntegerField('Total Projects', validators=[DataRequired()])
    image1 = FileField('Upload Image1', validators=[FileAllowed(['jpg', 'png', 'gif'], 'Images only!')])
    image2 = FileField('Upload Image2', validators=[FileAllowed(['jpg', 'png', 'gif'], 'Images only!')])
    submit = SubmitField('Submit Project')
