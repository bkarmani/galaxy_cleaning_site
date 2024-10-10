from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, URLField, SubmitField, DateTimeField
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
