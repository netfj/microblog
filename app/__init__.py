#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   __init__.py 
time:   2019/3/10.20:11
"""

from flask import Flask

app2 = Flask(__name__)

app2.config.from_object('config')

from app import views


