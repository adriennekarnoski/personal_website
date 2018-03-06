from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm
from flask_mail import Mail, Message
import os

mail = Mail()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')


mail.init_app(app)


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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(
                request.form['subject'],
                sender=os.environ.get('MAIL_SENDER'),
                recipients=[os.environ.get('MAIL_USERNAME')])
            msg.body = """
            Name: {}
            Email: {}


            Message: {}

            """.format(
                request.form['name'],
                request.form['email'],
                request.form['message'])
            mail.send(msg)
            return render_template('contact.html', form=None)
    return render_template('contact.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
