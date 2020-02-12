from django.shortcuts import render , redirect,  get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from . Serializers import shop_productsSerializer
from rest_framework.response import Response
from django.core.paginator import Paginator
from Ecommerece_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . import checksum

MERCHANT_KEY ="MERCHANT_KEY _HERE"


# Create your views here.

def Home(request):
	new_prod = New_prod_arrival.objects.all()
	flash_prod = Flash_latest_prod.objects.all()

	return render(request , 'home.html' , {'new_prod_arriaval': new_prod ,'flash_prods':flash_prod})



def About(request):
	return render(request , 'about.html')



def Shop(request):
	product = shop_products.objects.all()

	
	paginator = Paginator(product, 3)
	page = request.GET.get('page')
	shop_prod = paginator.get_page(page)

	num_page = paginator.page_range
	print(num_page)
	return render(request , 'shop.html', {'shop_prod':shop_prod, 'pages':num_page})



def men_collection(request,):

	men_collections = shop_products.objects.filter(category="Men")	

	paginator = Paginator(men_collections, 1) # Show 3 item per page
	page = request.GET.get('page')			  # Creating Page for next-page
	men_prods = paginator.get_page(page)  	  # 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Men_collection.html' ,{'men_prod':men_prods ,'pages':num_page})


def women_collection(request):

	men_collections = shop_products.objects.filter(category="Women")	

	paginator = Paginator(men_collections, 3) # Show 3 item per page
	page = request.GET.get('page')			  # Creating Page for next-page
	women_prods = paginator.get_page(page)  	  # 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Women_collection.html' ,{'women_prod':women_prods ,'pages':num_page})


def cloth_collection(request):

	men_collections = shop_products.objects.filter(category="Cloth")	

	paginator = Paginator(men_collections, 3) # Show 3 item per page
	page = request.GET.get('page')			  # Creating Page for next-page
	cloth_prods = paginator.get_page(page)  	  # 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Cloths.html' ,{'cloth_prod':cloth_prods ,'pages':num_page})


def acs_collection(request):

	men_collections = shop_products.objects.filter(category="Accesories")	

	paginator = Paginator(men_collections, 3) # Show 3 item per page
	page = request.GET.get('page')			  # Creating Page for next-page
	acs_prods = paginator.get_page(page)  	  # 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Accesories.html' ,{'acs_prod':acs_prods ,'pages':num_page})


def other_collection(request):

	men_collections = shop_products.objects.filter(category="Other")	

	paginator = Paginator(men_collections, 3) # Show 3 item per page
	page = request.GET.get('page')			  # Creating Page for next-page
	other_prods = paginator.get_page(page)  	  # 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Others.html' ,{'other_prod':other_prods ,'pages':num_page})




def prod_review(request, p_id):

	prod_rev = shop_products.objects.filter(id=p_id)
	new_prod = New_prod_arrival.objects.filter(id=p_id)

	return render(request , 'product_review.html' , {'see_prod':prod_rev, 'new_product':new_prod})





class Collection_api(APIView):

	def get(self , request):
		prod = shop_products.objects.all()
		serializer = shop_productsSerializer(prod , many=True)
		return Response(serializer.data)

	def post(self , request):
		pass






def Cart(request):
	return render(request , 'cart.html')



def Checkout(request):
	if request.method=="POST":
		f_name=request.POST['f_name']
		l_name=request.POST['l_name']
		country=request.POST['country']
		street=request.POST['street']
		town_city=request.POST['town']
		pin=request.POST['postal']
		phone=request.POST['phone']
		email=request.POST['email']
		ordr=order(firstName=f_name,laststName=l_name,country=country,address=street,town_city=town_city,postal=pin,phone=phone,email=email)
		ordr.save()
    

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})




def Blog(request):
	return render(request , 'blog.html')



def Single_blog(request):
	return render(request , 'blog-single.html')



def Single_product(request):
	return render(request , 'product_review.html')



def Contact(request):	

	if request.method=='POST':
		name=request.POST['Name']
		email=request.POST['Mail']
		subject=request.POST['Subject']
		msg=request.POST['Msg']
		message='Name: '+name+'\n'+'Email: '+ email+'\n'+'Message: '+msg
		print(message)
		recepient = ['21sarfrazansari@gmail.com']
		send_mail(subject,message, EMAIL_HOST_USER, recepient)
    	#print("Email send Succesfully!")
    	#return redirect('/contact')	
	else:
		pass
	return render(request, 'contact.html')

def New_acount(request):

	if request.method =="POST":
		f_name = request.POST['f_name']
		l_name = request.POST['l_name']
		email = request.POST['email']
		u_name = request.POST['u_name']
		pswd1 = request.POST['pswd1']
		pswd2 = request.POST['pswd2']

		print(pswd1, pswd2 ,email)

		if (pswd1!=pswd2):
			messages.info(request, 'Password is not matching !')
			return redirect('/acount/new_acount/')
			
		else:
			if User.objects.filter(username=u_name).exists():
				messages.info(request, 'Username allready exists kindly Login')
				return redirect('/acount/login/')
				print('Login redirect')
			else:
				usr = User.objects.create_user(first_name=f_name, last_name=l_name,password=pswd1, username=u_name)
				usr.save()
				print("User hae been created")
				messages.info(request ,'User acount has been created !')
				return redirect('/acount/login/')

	return render(request, 'Signup.html')





def Login(request):

	if request.method =='POST':
		uname = request.POST['uname']
		pswd = request.POST['psw']

		user = auth.authenticate(username=uname,password=pswd)

		if user is not None:
			auth.login(request, user)
			return redirect('/')

		else:
			messages.error(request, 'kindly enter right credentials')
			return redirect('/acount/login/')
	
	else:
		return render(request, 'Login.html')

def Logout(request):
	auth.logout(request)
	return redirect('/')

