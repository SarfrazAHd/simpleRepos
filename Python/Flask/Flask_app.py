from flask import Flask , render_template, request, flash , session ,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import math
from datetime import datetime

app = Flask(__name__)


app.config.update(
MAIL_SERVER = 'smtp.gmail.com', 
MAIL_PORT =   465,
MAIL_USE_SSL  = True, 
MAIL_USERNAME = 'sarafraj.ahmad@galgotiasuniversity.edu.in',
MAIL_PASSWORD = 'Sarfraz@786')

mail = Mail(app)

app.secret_key = 'the-secret-keys'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\21sar\\OneDrive\\Desktop\\Flask\\Badprogrammer.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Contact_db(db.Model):
	Id = db.Column(db.Integer , primary_key = True)
	Name = db.Column(db.String(80), unique=True, nullable=True)
	Email = db.Column(db.String(130), unique=True, nullable=True)
	Phone = db.Column(db.String(130), unique=True, nullable=False)
	Messages = db.Column(db.String(130), unique=True, nullable=False)




class Post_db(db.Model):
	Id = db.Column(db.Integer , primary_key = True)
	Title = db.Column(db.String(80), unique=True, nullable=True)
	Subtitle = db.Column(db.String(130), unique=False, nullable=True)
	Content = db.Column(db.String(130), unique=False, nullable=True)
	Slug = db.Column(db.String(130), unique=True, nullable=True)
	Date = db.Column(db.String(130), unique=False, nullable=True)
	







@app.route('/', methods=["GET"])
def Home():

	posts = Post_db.query.filter_by().all()
	last = math.ceil(len(posts)/ 2)
	#posts = list(posts)

	page = request.args.get('page')

	if( not str(page).isnumeric()):
		page = 1

	page = int(page)
	posts = posts[(page-1) *2: (page-1) *2 +2]

	if(page ==1):
		prev = "#"
		nexts = "/?page=" + str(page+1) 

	elif(page ==last):
		nexts = "#"
		prev = "/?page=" + str(page-1) 

	else:
		prev = "/?page=" + str(page-1) 
		nexts = "/?page=" + str(page+1) 

	return render_template('index.html', tag= "Badprogrammer", Post=posts, previous=prev, nex=nexts)




@app.route("/Admin", methods=["GET", "POST"])
def Admin_page():

	Admin_user = 'Admin'
	Admin_password = 'Admin'


	if ('user' in session and session['user'] == Admin_user):
		posts = Post_db.query.filter_by().all()
		return render_template('Admin_dashboard.html',Post = posts)


	if request.method =="POST":
		usrname = request.form.get('username')
		password = request.form.get('password')

		if(usrname == Admin_user and password == Admin_password):

			session['user'] = usrname
			posts = Post_db.query.filter_by().all()
			return render_template("Admin_dashboard.html", Post=posts)



		else:
			return render_template("Admin_login.html")
	else:
		return render_template("Admin_login.html")




@app.route('/about')
def about():
	return render_template('about.html')





@app.route('/contact', methods=["GET", "POST"])
def contact():

	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	msg = request.form.get('message')


	if name =='' or email=='' or phone =='' or msg =='':
		flash("Kindly Enter Your all query Details!" , 'danger')

	else:


		if (request.method == "POST"):
		
			#entry = Contact_db( Name = name, Phone=phone, Email = email, Messages = msg)
			#db.session.add(entry)
			#db.session.commit()

			mail.send_message("Message from " + name,
	                  sender=email,
	                  recipients=["sarafraj.ahmad@galgotiasuniversity.edu.in"], 
	                  body = 'Message :'+ msg + "\nPhone:" + phone)

			flash("Your message has been sent successfully!", 'success')

		return render_template('contact.html')





@app.route('/Post/<string:post_slug>', methods=["GET"])
def post(post_slug):

	Post_query = Post_db.query.filter_by(Slug=post_slug).first()
	return render_template('post.html',Post=Post_query)



@app.route('/Edit_post/<string:Id>', methods=["GET", "POST"])
def Edit_post(Id):


	Admin_user = 'Admin'
	Admin_password = 'Admin'


	if ('user' in session and session['user'] == Admin_user):
		if request.method =="POST":
			title = request.form.get('Title')
			subtitle = request.form.get('Subtitle')
			date = request.form.get('Date')
			content = request.form.get('Content')
			slug = request.form.get('slug')

			if Id != '0':
				post = Post_db.query.filter_by(Id= Id).first()
				post.Title = title
				post.Subtitle = subtitle
				post.Date = date
				post.Content = content
				post.Slug = slug
				db.session.commit()

				return redirect('/Edit_post/'+ Id)

	else:
		return render_template("Admin_login.html")

	post = Post_db.query.filter_by(Id= Id).first()
	return render_template('Edit_post.html', post= post)





@app.route('/Admin/new_post',  methods=["GET", "POST"])
def add_new_post():

	Admin_user = 'Admin'
	Admin_password = 'Admin'

	if (request.method == "POST" or "GET") and ('user' in session and session['user'] == Admin_user):
		title = request.form.get('title')
		subtitle = request.form.get('subtitle')
		date = request.form.get('date')
		content = request.form.get('content')
		slug = request.form.get('slug')

		post = Post_db(Title =title, Subtitle =subtitle , Date =date, Content = content, Slug = slug)
		db.session.add(post)
		db.session.commit()
	else:
		return render_template("Admin_login.html")

	return render_template('new_post.html')


@app.route('/Delete_post/<string:Id>', methods=["GET", "POST"])
def Delete_post(Id):

	Admin_user = 'Admin'
	Admin_password = 'Admin'

	if(request.method =="GET" or "POST") and ('user' in session and session['user'] == Admin_user):
		post = Post_db.query.filter_by(Id = Id).first()
		db.session.delete(post)
		db.session.commit()

	else:
		return render_template("Admin_login.html")


	return redirect('/Admin')




@app.route('/Logout') 
def logout_window():

	session.clear()
	return render_template("Admin_login.html")



app.run(debug=True)

