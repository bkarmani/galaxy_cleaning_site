from flask import url_for, redirect, render_template
from . import admin



@admin.route('/dashboard')
def dash():
    return render_template('admin/layout.html')

