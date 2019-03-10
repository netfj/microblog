#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   views.py
time:   2019/3/10.20:10
"""

from flask import render_template, flash, redirect
from app import app2
from .forms import LoginForm

# index view function suppressed for brevity

@app2.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)