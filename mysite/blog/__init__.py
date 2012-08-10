# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import settings


app = Flask(__name__)

# Add Config to flask
app.config.from_object(settings)

# Set the sqlalchemy object
db = SQLAlchemy(app)

# Import the tables
import models

# Import all the views
import views
