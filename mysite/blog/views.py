# -*- coding: utf-8 -*-

from blog import app

@app.route('/')
def index():
    return 'Hello World!'
