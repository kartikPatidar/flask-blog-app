from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user= {'username': 'Michale'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",title="Home", user=user, posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if it is a POST request and all data is valid(implemented using validators in forms.py)
    # then below line returns true.
    if form.validate_on_submit():
        # flash generated message which can be shown to user
        # temperary solution for now as we don't have infrastructure yet to login user.  
        flash("Login requested for user {}, remeber_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)
    