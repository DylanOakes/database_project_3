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
        email = request.form['email']
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

@main.route('/users/delete/<string:user_id>')
def delete_user(user_id):
    user = users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted!', 'warning')
    return redirect(url_for('main.users'))

@main.route('/assignments')
def assignments():
    data = a_status.query.all()
    return render_template('assignments.html', assignments=data)

@main.route('/assignments/add', methods=['GET', 'POST'])
def add_assignment():
    u_list = users.query.all()

    if request.method == 'POST':
        task_id = request.form['task_id']
        user_id = request.form['user_id']
        task_name = request.form['task_name']
        task_desc = request.form['task_desc']
        is_complete = request.form['is_complete']
        due_date = request.form['due_date']

        if not task_id.strip():
            flash('Task ID is required.', 'error')
            return redirect(url_for('main.add_assignment'))

        if not task_name.strip():
            flash('Task Name is required.', 'error')
            return redirect(url_for('main.add_assignment'))
        
        try:
            detail = a_details(TaskID=task_id, TaskName=task_name, TaskDesc=task_desc)
            db.session.add(detail)
            db.session.flush()

            assignment_status = a_status(TaskID=task_id, UserID=user_id, isComplete=is_complete, DueDate=due_date)
            db.session.add(assignment_status)
            db.session.commit()

            flash('Assignment added successfully', 'success')
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding assignment: {str(e)}', 'error')
        
        return redirect(url_for('assignments.html'))

## @main.route("/")
## def index():
##    records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
##    return render_template("index.html", records=records)

