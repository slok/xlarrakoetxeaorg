from blog import app

app.run(debug=app.config['DEBUG'], host=app.config['HOST'])