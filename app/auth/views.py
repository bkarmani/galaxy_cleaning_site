from . import auth
from flask import render_template, redirect, url_for, request, flash
from .forms import login_form, RegistrationForm
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User
from .. import db
from ..emails import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = form.password.data
        if user is not None and user.verify_password(password):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
                flash('you have successfully logged in', category='success')
            return redirect(next)
        flash('invalid username or password', category='danger')
    return render_template('auth/login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
            )
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        # send_email(user.email,'Confirm Your Account',
        #            'auth/email/confirm', user=user,token=token)
        flash('a confirmation email have been sent to you by email')
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out successfuly', category='success')
    return redirect(url_for('main.index'))