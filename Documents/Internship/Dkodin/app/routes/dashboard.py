from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.task import Task
dashboard_bp = Blueprint('dashboard', __name__)
@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    total_tasks = len(tasks)
    completed = len([t for t in tasks if t.status == "Completed"])
    pending = len([t for t in tasks if t.status == "Pending"])
    return render_template(
        'dashboard/index.html',
        tasks=tasks,
        total=total_tasks,
        completed=completed,
        pending=pending
    )
