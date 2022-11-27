from flask import Blueprint, render_template

logins = Blueprint("login", __name__)


@logins.route('/login/', methods=["GET", "POST"])
def login():
    return render_template('login.html')