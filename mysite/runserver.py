# -*- coding: utf-8 -*-

from blog import app

app.run(debug=app.config['DEBUG'], host=app.config['HOST'])