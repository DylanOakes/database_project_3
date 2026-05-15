from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from .extensions import db

from .models import (
    users,
    a_details,
    a_status,
    team_det,
    team_mem
)

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route('/users')
def users():
    all_users = users.query.all()
    return render_template('users.html', users=all_users)

@main.route('/users/add', methods=['GET', 'POST'])
def add_users():
    if request.method == 'POST':
        user_id = request.form['user_id']
        username = request.form['username']
        Email = request.form['email']
        phone_num = request.form['phone_num']
        join_date = request.form['join_date']
    
        if not user_id.strip():
            flash('User ID is required.', 'error')
            return redirect(url_for('main.add_users'))
        
        if not username.strip():
            flash('Username is required.', 'error')
            return redirect(url_for('main.add_users'))
        
        if not email.strip():
            flash('Email is required.', 'error')
            return redirect(url_for('main.add_users'))
        
        if users.query.filter_by(email = Email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('main.add_users'))
        
        new_user = users(UserID=user_id, UserName=username, email=Email, PhoneNum=phone_num, JoinDate=join_date)
        
        db.session.add(new_user)
        db.session.commit()

        flash('User added!')
        return redirect(url_for('main.users'))
    
    return render_template('add_users.html')

## @main.route("/")
## def index():
##    records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
##    return render_template("index.html", records=records)

