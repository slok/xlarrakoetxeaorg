from flask import Flask

import settings


app = Flask(__name__)

# Add Config to flask
app.config.from_object(settings)

# Import all the views
import views
