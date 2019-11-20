from flask import Flask, render_template

app = Flask(__name__)


@app.route('/Login')
def login_page():
	return render_template('Login_from.html')


@app.route('/')
def home():

	return "Hello From Flask-2"


@app.route('/template')
def index():
	return render_template('Template.html')



@app.route('/img')
def image():
	return render_template('1.html')


app.run(debug = True)