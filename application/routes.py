from application import app
from flask import render_template, request, flash, redirect, url_for
from application.form import UserInputForm
from datetime import datetime
from application.models import WorkTime
from application import db
import json

@app.route("/")
def index():
    entries = WorkTime.query.order_by(WorkTime.date.desc()).all()
    return render_template('index.html', title = 'index', entries = entries)

@app.route("/add", methods = [ "GET", "POST"])
def add_worktime():
    form = UserInputForm()
    if form.validate_on_submit():       # form validation
        
        time_in = form.time_in.data
        time_out = form.time_out.data
        
        # Calculate total hours worked for the day
        total_hours_day = (datetime.combine(datetime.min, time_out) - 
                           datetime.combine(datetime.min, time_in)).seconds / 3600
        if total_hours_day < 0:
            total_hours_day += 24
        
        # Assuming days_worked is sent in the form
        days_worked = request.form.get('days_worked', 1, type=int)
        
        # Calculate total hours worked for the month
        total_hours_month = total_hours_day * days_worked
        entry = WorkTime(type=form.type.data, name=form.name.data, time_in=form.time_in.data, time_out=form.time_out.data, month=form.month.data, date=form.date.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"successful entrys", "success")
        return redirect(url_for('index'))
    return render_template("add.html", title = 'add time', form = form)

@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = WorkTime.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))
    

