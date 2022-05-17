from __init__ import app, socket
import sys

from flask import render_template, request, redirect, make_response
from flask import flash
from __init__ import app  # ,socket
from flask_socketio import emit


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def test():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('base.html')
