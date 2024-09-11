import requests
from flask import request, render_template
from flask_mail import Message
from . import email

def subscribe_user(email, user_group_email, api_key ):
    
    resp = requests.post(f'https://api.mailgun.net/v3/lists/{user_group_email}/members',
                         auth = ('api', api_key),
                         data = {'subscribed':True, 'address':email}
                        )
    
    return resp

# def send_email(sender_email, reciever_email, password):
#     sender = sender_email
#     receiver = reciever_email

#     message = f"""\
#     Subject: Hi Mailtrap
#     To: {receiver}
#     From: {sender}

#     This is a test e-mail message."""


#     with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
#         server.login("58eb16ba86f01f", password)
#         server.sendmail(sender, receiver, message)

def send_email(subject, sender, recipient, template,  **kwargs):
    msg = Message(subject, sender=sender, recipients=[recipient])  
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    email.send(msg)
    