from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from app.extensions import db
profile_bp = Blueprint('profile', __name__)
@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        # Basic validation
        if not name or not phone:
            flash("All fields are required", "danger")
            return redirect('/profile')
        # Update user details
        current_user.name = name
        current_user.phone = phone
        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect('/profile')
    return render_template('profile/profile.html')
