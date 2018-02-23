from flask import Flask, render_template
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(__name__)

health = HealthCheck()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about_me.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

app.add_url_rule(
    "/healthcheck",
    "healthcheck",
    view_func=lambda: health.run())

