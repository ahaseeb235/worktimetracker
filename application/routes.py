from application import app
from flask import render_template
from application.form import UserInputForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/addtime")
def add_worktime():
    form = UserInputForm()
    return render_template("addtime.html", title = 'addtime', form = form)
