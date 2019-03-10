#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   forms.py
time:   2019/3/10.22:26
"""

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

