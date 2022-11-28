from flask import Blueprint, render_template

indexx=Blueprint("index",__name__)


@indexx.route('/')
def index():
    return render_template('index.html')