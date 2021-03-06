from os import environ
from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']=environ['SECRET']

def app_factory():
#view routes
    from .views import (index , todate)
    app.add_url_rule('/' , view_func = index)
    app.add_url_rule('/date' , view_func = todate)
    return app
