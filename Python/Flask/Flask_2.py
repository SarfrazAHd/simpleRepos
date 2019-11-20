from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('Login_from.html')

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/post')
def post():
	return render_template('post.html')


app.run(debug=True)


