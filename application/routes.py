from application import app
from flask import render_template, request, flash, redirect, url_for
from application.form import UserInputForm
from datetime import datetime

@app.route("/")
def index():
    return render_template('index.html')

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
        # entry = WorkTime(type=form.type.data, name=form.name.data, time_in=form.time_in.data, time_out=form.time_out.data, month=form.month.data, date=form.date.data)
        # db.session.add(entry)
        # db.session.commit()
        flash(f"successful entrys", "success")
        return redirect(url_for('index'))
    return render_template("add.html", title = 'add time', form = form)

