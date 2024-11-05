from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField, EmailField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Email, Length, Regexp, NumberRange


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

    # Select field for approximate square footage
    approx_sf = DecimalField(
        'Area or Count', 
        validators=[
            DataRequired(),
            NumberRange(min=1, message="Please enter a positive number.")
        ]
    )

    # Text field for budget
    budget = DecimalField(
        'Budget', 
        render_kw={"placeholder": "£ Budget"}, 
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Budget must be a positive number")
        ]
    )

    # Text field for ZIP Code
    zip_code = StringField(
        'Postcode', 
        validators=[
            DataRequired(message="Postcode is required"),
            Regexp(
                r'^[A-Z]{1,2}\d{1,2}[A-Z]?\s?\d[A-Z]{2}$', 
                message="Enter a valid UK postcode"
            )
        ]
    )

    #pets information
    pet_count = DecimalField(
        'no of pets', 
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Please enter a positive number.")
        ]
    )

    # Date and time fields for service appointment
    date = DateField('Preferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Preferred Time', format='%H:%M', validators=[DataRequired()])

    # Contact details fields
    name = StringField(
        'Name', 
        validators=[
            DataRequired(),
            Regexp(r'^[A-Za-z\s\-]+$', message="Name must contain only letters, spaces, or hyphens"),
            Length(min=2, max=50, message="Name must be between 2 and 50 characters")
        ]
    )

    phone = StringField(
        'Phone', 
        validators=[
            DataRequired(), 
            Regexp(r'^\d+$', message="Phone number must contain only digits")
        ]
    )

    email = StringField('Email', validators=[DataRequired(), Email()])

    # Text area fields for address and additional comments
    address = TextAreaField('Address', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired()])

    # Submit button
    submit = SubmitField('Request Now')




    

    






