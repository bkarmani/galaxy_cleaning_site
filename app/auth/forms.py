from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length,  Regexp, EqualTo
from ..models import User



class login_form(FlaskForm):
    email = StringField ('enter email', validators=[DataRequired(), Length(1, 64),\
                                                     Email()]) 
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('submit')


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('username', validators=[
        DataRequired(), Length(1,64),
        Regexp( '^[A-Za-z][A-Za-z0-9_.]*$', 0,
                'Usernames must have only letters, numbers, dots or '
                'underscores' )])
    password = PasswordField('password', validators=[
        DataRequired(), EqualTo('password2', message='passwords must match')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('signup')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email is already registered')
        
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username has been taken by another user')