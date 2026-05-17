from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from .extensions import db
import datetime
#from datetime import date

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
def get_users():
    items = db.select(users)
    all_users = db.session.execute(items).scalars().all()
    return render_template('users.html', users=all_users)


@main.route('/users/add', methods=['GET', 'POST'])
def add_users():
    if request.method == 'POST':
        user_id = request.form['user_id']
        username = request.form['username']
        email = request.form['email']
        phone_num = request.form['phone_num']
        join_date = datetime.datetime.strptime(request.form['join_date'], '%Y-%m-%d').date()

        if not user_id.strip():
            flash('User ID is required.', 'error')
            return redirect(url_for('main.add_users'))

        if not username.strip():
            flash('Username is required.', 'error')
            return redirect(url_for('main.add_users'))
        
        if not email.strip():
            flash('Email is required.', 'error')
            return redirect(url_for('main.add_users'))
        
        existing_user = select(users).where(users.Email == email)
        existing_user = db.session.execute(existing_user).scalar_one_or_none()
        if existing_user:
            flash('Email already exists.', 'error')
            return redirect(url_for('main.add_users'))
        
        new_user = users(UserID=user_id, UserName=username, Email=email, PhoneNum=phone_num, JoinDate=join_date)
        db.session.add(new_user)
        db.session.commit()

        flash('User added!')
        return redirect(url_for('main.get_users'))
    
    return render_template('users.html')

@main.route('/users/delete/<string:user_id>')
def delete_user(user_id):
    user = users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted!', 'warning')
    return redirect(url_for('main.get_users'))


@main.route('/assignments')
def assignments():
    all_assignments = db.session.query(
        a_status.TaskID,
        a_status.UserID,
        a_details.TaskName,
        a_details.TaskDesc,
        a_status.isComplete,
        a_status.DueDate
    ).join(
        a_details,
        a_status.TaskID == a_details.TaskID
    ).all()
    
    #items= db.select(a_details).join(a_status, a_details.TaskID == a_status.TaskID)
    #all_assignments = db.session.execute(items).scalars().all()
    return render_template('assignments.html', tasks=all_assignments)

@main.route('/assignments/add', methods=['GET', 'POST'])
def add_assignment():
    if request.method == 'POST':
        task_id = request.form['task_id']
        user_id = request.form['user_id']
        task_name = request.form['task_name']
        task_desc = request.form['task_desc']
        is_complete = request.form['is_complete']
        due_date = datetime.datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()

        existing_assignment = select(a_status).where(a_status.TaskID == task_id and a_status.UserID == user_id)
        existing_assignment = db.session.execute(existing_assignment).scalar_one_or_none()
        if existing_assignment:
            flash('This assignment is already assigned to the given user', 'error')
            return redirect(url_for('main.add_assignment'))

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
        
        return redirect(url_for('main.assignments'))
    return render_template('assignments.html')


@main.route('/assignments/delete/<string:task_id>/<string:user_id>')
def delete_assignment(task_id, user_id):
    task = a_status.query.get_or_404((task_id, user_id))
    
    db.session.delete(task)
    db.session.commit()

    flash('Assignment deleted', 'warning')
    return redirect(url_for('main.assignments'))


@main.route('/teams')
def teams():
    all_teams = db.session.query(
        team_mem.TeamID,
        team_mem.UserID,
        team_det.TeamName,
        team_mem.TeamJoinDate
    ).join(
        team_det,
        team_mem.TeamID == team_det.TeamID
    ).all()

    #all_teams = team_det.query.all()
    return render_template('teams.html', teams=all_teams)

@main.route('/teams/add', methods=['GET', 'POST'])
def add_team():

    if request.method == 'POST':
        t_id = request.form['team_id']
        u_id = request.form['user_id']
        t_name = request.form['team_name']
        join_date = datetime.datetime.strptime(request.form['join_date'], '%Y-%m-%d').date()

        existing_team = select(team_mem).where(team_mem.TeamID == t_id and team_mem.UserID == u_id)
        existing_team = db.session.execute(existing_team).scalar_one_or_none()
        if existing_team:
            flash('This user is already assigned to the given team', 'error')
            return redirect(url_for('main.add_team'))

        if not t_id.strip():
            flash('Team ID is required.', 'error')
            return redirect(url_for('main.add_team'))
        
        if not u_id.strip():
            flash('User ID is required.', 'error')
            return redirect(url_for('main.add_team'))

        if not t_name.strip():
            flash('Team Name is required.', 'error')
            return redirect(url_for('main.add_team'))

        teams = team_det(TeamID=t_id, TeamName=t_name)
        db.session.add(teams)
        db.session.flush()

        members = team_mem(TeamID=t_id, UserID=u_id, TeamJoinDate=join_date)
        db.session.add(members)
        db.session.commit()

        flash('Team added successfully', 'success')
        return redirect(url_for('main.teams'))
    
    return render_template('teams.html')


@main.route('/teams/delete/<string:team_id>/<string:user_id>')
def delete_team(team_id, user_id):
    team = team_mem.query.get_or_404((team_id, user_id))
    db.session.delete(team)
    db.session.commit()

    flash('Team member removed', 'warning')
    return redirect(url_for('main.teams'))