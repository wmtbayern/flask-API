import requests
from flask import Blueprint, render_template, redirect, url_for, request
from flask.json import jsonify

from app.exts import cache
from app.models import User

blue=Blueprint('blue',__name__)

def init_view(app):

    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():

    # data=requests.get(url='http://127.0.0.1:5000/api/v1/banners/')
    # print(data)


    try:
        token=cache.get('token')
        userid=User.query.get(token=token)
        users=User.query.filter(User.id==userid)
        user=users.first()
        return render_template('index.html',user=user)
    except:
        return render_template('index.html',)

@blue.route('/login/')
def login():
    if request.method=='GET':
        return render_template('login.html')


@blue.route('/logout/')
def logout():

    cache.delete('token')

    return redirect(url_for('blue.index'))

@blue.route('/register/')
def register():

    return render_template('register.html')