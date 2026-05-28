from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.task import Task
task_bp = Blueprint('task', __name__)
# View all tasks
@task_bp.route('/tasks')
@login_required
def tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('task/tasks.html', tasks=tasks)
# Add new task
@task_bp.route('/add-task', methods=['POST'])
@login_required
def add_task():
    title = request.form['title']
    description = request.form['description']
    if not title:
        flash("Task title is required", "danger")
        return redirect('/tasks')
    task = Task(
        title=title,
        description=description,
        user_id=current_user.id
    )
    db.session.add(task)
    db.session.commit()
    flash("Task added successfully!", "success")
    return redirect('/tasks')
# Update status
@task_bp.route('/update-task/<int:id>')
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    if task.status == "Pending":
        task.status = "In Progress"
    elif task.status == "In Progress":
        task.status = "Completed"
    db.session.commit()
    return redirect('/tasks')
# Delete task
@task_bp.route('/delete-task/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted", "warning")
    return redirect('/tasks')
