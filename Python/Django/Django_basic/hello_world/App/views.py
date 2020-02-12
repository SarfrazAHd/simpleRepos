from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Destination


# Create your views here.

def Index(request):

	dest = Destination.objects.all()

	return render(request, 'index.html', {'dest': dest, 'title':'Home Travello'})

							
def About(request):
	return render(request, 'about.html')


def Services(request):
	return render(request, 'destinations.html')


def News(request):
	return render(request, 'news.html')

def Contact(request):
	return render(request, 'contact.html')




def Sign_up(request):

	if request.method =="POST":

		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		uname = request.POST['uname']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if (password1 == password2):

			if User.objects.filter(username=uname).exists():
				messages.info(request, "Username is allready taken")
				return redirect('/signup')


			elif User.objects.filter(email=email).exists():
				messages.info(request, "Email is allready taken")
				return redirect('/signup')

			else:

				user = User.objects.create_user(first_name=fname, 
					last_name=lname,password=password1,email=email,
					username=uname)

				user.save()   
				return redirect('/login')

		else:
			messages.error(request, "Password is not matching")
			return redirect('/signup')

	else:
		return render(request, 'signup_form.html')
	

def Login(request):

	if request.method =="POST":
		uname = request.POST['uname']
		pwd = request.POST['password']

		user = auth.authenticate(username=uname, password=pwd)

		if user is not None:

			auth.login(request, user)

			return redirect('/dashboard')

		else:
			messages.error(request, "Invalid Credentials")
			return redirect('/login')

	else:
		return render(request, 'login_form.html')




def Dashboard(request):

	if request.user.is_authenticated:
		return render(request, 'dashboard.html')

	else:
		messages.error(request,"Kindly login first !")
		return redirect('/login')


def Logout(request):

	auth.logout(request)
	return redirect('/login')








