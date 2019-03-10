#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   views.py
time:   2019/3/10.20:10
"""
from flask import render_template
from app import app2

@app2.route('/index0')
def index0():
    return "Hello, World! 002"


@app2.route('/html0/')
def html0():
    user = {'nickname': 'Miguel'}  # fake user
    return '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
      </body>
    </html>
    '''

@app2.route('/')
@app2.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='示例',
                           user=user,
                           posts=posts)