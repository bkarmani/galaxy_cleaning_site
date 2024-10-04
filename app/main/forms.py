from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField, EmailField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


# class NewsLetterForm(FlaskForm):
#     email = EmailField(' your email address', validators=[DataRequired(), Email(), Length(1,64)])
#     submit = SubmitField('Subscribe now')

# class RequestServiceForm(FlaskForm):
#     name = StringField('your name', validators=[DataRequired()])
#     email = EmailField(' your email address', validators=[DataRequired(), Email(), Length(1,64)])
#     phone = StringField('phone number', validators=[DataRequired()])
#     date = DateTimeField('date here')
#     submit = SubmitField('Get Service')


# class AppointmentForm(FlaskForm):
#     name = StringField('user\'s name', validators=[DataRequired()])
#     email = EmailField(' your email address', validators=[DataRequired(),
#                  Email(), Length(1,64)])
#     phone_number = StringField('phone number')
#     address = StringField('address', validators=[DataRequired()])
#     service = SelectField('choose services', choices=['services 1', 'services 2', 'services 3', 'services 4'], validators=[DataRequired()])
#     date = DateTimeField('date', validators=[DataRequired()])
#     comment = TextAreaField('comments')
#     submit = SubmitField('submit')

# class ReviewForm(FlaskForm):
#     name = StringField('your name*', validators=[DataRequired()])
#     email =  StringField('email', validators=[DataRequired(), 
#                 Email(), Length(1,64)])
#     phone = StringField('Phone Number')
#     review = TextAreaField('Your Review*', validators=[DataRequired()])
#     submit = SubmitField('leave your review')

# class ContactForm(FlaskForm):
#     name = StringField('your name*', validators=[DataRequired()])
#     email =  StringField('email', validators=[DataRequired(), 
#                 Email(), Length(1,64)])
#     phone = StringField('Phone Number')
#     question = TextAreaField('question')
#     submit = SubmitField('leave your questions')


# # class RequestEstimate(FlaskForm):

class QuotesForm(FlaskForm):
    # Select field for cleaning service type
    cleaning_service = SelectField('Cleaning Service', choices=[
        ('0', 'Residential cleaning'),
        ('1', 'Commercial cleaning'),
        ('2', 'Custom cleaning'),
        ('3', 'Green cleaning'),
        ('4', 'Sanitization & Disinfection'),
        ('5', 'Car Wash'),
        ('6', 'Specialized Cleaning')
    ], validators=[DataRequired()])

    # Select field for type of property
    property_type = SelectField('Property Type', choices=[
        ('0', 'Apartment'),
        ('1', 'Office Space'),
        ('2', 'Car'),
        ('3', 'Rugs'),
        ('4', 'A particular Space'),
        ('5', 'Other')
    ], validators=[DataRequired()])

    # Select field for approximate square footage
    approx_sf = SelectField('Area in SF', choices=[
        ('0', '-- Approx SF --'),
        ('1', '400'),
        ('2', '200'),
        ('3', '600'),
        ('4', '300')
    ], validators=[DataRequired()])

    # Text field for budget
    budget = StringField('Budget', render_kw={"placeholder": "£ Budget"})

    # Text field for ZIP Code
    zip_code = StringField('ZIP Code', validators=[DataRequired()])

    # Date and time fields for service appointment
    date = DateField('Preferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Preferred Time', format='%H:%M', validators=[DataRequired()])

    # Contact details fields
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Text area fields for address and additional comments
    address = TextAreaField('Address', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired()])

    # Submit button
    submit = SubmitField('Request Now')




    

    






