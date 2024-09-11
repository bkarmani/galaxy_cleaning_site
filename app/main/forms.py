from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, EmailField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class NewsLetterForm(FlaskForm):
    email = EmailField(' your email address', validators=[DataRequired(), Email(), Length(1,64)])
    submit = SubmitField('Subscribe now')

class RequestServiceForm(FlaskForm):
    name = StringField('your name', validators=[DataRequired()])
    email = EmailField(' your email address', validators=[DataRequired(), Email(), Length(1,64)])
    phone = StringField('phone number', validators=[DataRequired()])
    date = DateTimeField('date here')
    submit = SubmitField('Get Service')


class AppointmentForm(FlaskForm):
    name = StringField('user\'s name', validators=[DataRequired()])
    email = EmailField(' your email address', validators=[DataRequired(),
                 Email(), Length(1,64)])
    phone_number = StringField('phone number')
    address = StringField('address', validators=[DataRequired()])
    service = SelectField('choose services', choices=['services 1', 'services 2', 'services 3', 'services 4'], validators=[DataRequired()])
    date = DateTimeField('date', validators=[DataRequired()])
    comment = TextAreaField('comments')
    submit = SubmitField('submit')

class ReviewForm(FlaskForm):
    name = StringField('your name*', validators=[DataRequired()])
    email =  StringField('email', validators=[DataRequired(), 
                Email(), Length(1,64)])
    phone = StringField('Phone Number')
    review = TextAreaField('Your Review*', validators=[DataRequired()])
    submit = SubmitField('leave your review')

class ContactForm(FlaskForm):
    name = StringField('your name*', validators=[DataRequired()])
    email =  StringField('email', validators=[DataRequired(), 
                Email(), Length(1,64)])
    phone = StringField('Phone Number')
    question = TextAreaField('question')
    submit = SubmitField('leave your questions')

    

    






