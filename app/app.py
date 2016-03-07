#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime


app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
        return render_template('500.html'), 500

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/bad')
def bad():
    return '<h1> Bad Request</h1>', 400


@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie! </h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<id>')
def get_user(id):
    pass


@app.route('/redirect')
def redirect_to():
        return redirect('http://www.sina.com.cn')

if __name__ == '__main__':
    app.run(debug=True)