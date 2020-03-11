
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
from django.views.decorators.csrf import csrf_exempt
from . import Checksum


MERCHANT_KEY='FMKeQY97hgV_y@cV'

# Create your views here.
def Home(request):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	new_prod = shop_products.objects.filter(category="New_product")
	flash_prod = Flash_latest_prod.objects.all()

	return render(request , 'home.html' , {'new_prod_arriaval': new_prod ,'flash_prods':flash_prod,'total_item':total_itm})



def About(request):
	return render(request , 'about.html')



def Shop(request):
	
	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	product = shop_products.objects.all()
	
	paginator = Paginator(product,9)
	page = request.GET.get('page')
	shop_prod = paginator.get_page(page)

	num_page = paginator.page_range
	print(num_page)
	return render(request , 'shop.html', {'shop_prod':shop_prod, 'pages':num_page,'total_item':total_itm})



def men_collection(request,):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	men_collections = shop_products.objects.filter(category="Men")	

	paginator = Paginator(men_collections, 6) 		# Show 6 item per page
	page = request.GET.get('page')			  		# Creating Page for next-page
	men_prods = paginator.get_page(page)  	  		# 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Men_collection.html' ,{'men_prod':men_prods ,'pages':num_page,'total_item':total_itm})


def women_collection(request):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	men_collections = shop_products.objects.filter(category="Women")	

	paginator = Paginator(men_collections, 6) 		# Show 6 item per page
	page = request.GET.get('page')			  		# Creating Page for next-page
	women_prods = paginator.get_page(page)  	  	# 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Women_collection.html' ,{'women_prod':women_prods ,'pages':num_page,'total_item':total_itm})


def cloth_collection(request):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	men_collections = shop_products.objects.filter(category="Cloth")	

	paginator = Paginator(men_collections, 6) 		# Show 6 item per page
	page = request.GET.get('page')			  		# Creating Page for next-page
	cloth_prods = paginator.get_page(page)  	  	# 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Cloths.html' ,{'cloth_prod':cloth_prods ,'pages':num_page,'total_item':total_itm})


def acs_collection(request):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	men_collections = shop_products.objects.filter(category="Accesories")	

	paginator = Paginator(men_collections, 6) 		# Show 6 item per page
	page = request.GET.get('page')			  		# Creating Page for next-page
	acs_prods = paginator.get_page(page)  	  		# 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Accesories.html' ,{'acs_prod':acs_prods ,'pages':num_page,'total_item':total_itm})


def other_collection(request):

	cart_product = cart.objects.all()
	total_itm = len(cart_product)

	men_collections = shop_products.objects.filter(category="Other")	

	paginator = Paginator(men_collections, 6) 		# Show 6 item per page
	page = request.GET.get('page')			  		# Creating Page for next-page
	other_prods = paginator.get_page(page)  		# 

	# Number of page in Page
	num_page = paginator.page_range
	return render(request , 'Others.html' ,{'other_prod':other_prods ,'pages':num_page,'total_item':total_itm})




def prod_review(request, p_id):

	prod_rev = shop_products.objects.filter(id=p_id)
	cart_product = cart.objects.all()
	total_itm = len(cart_product)
	return render(request , 'product_review.html' , {'new_product':prod_rev,'total_item':total_itm})


class Collection_api(APIView):

	def get(self , request):
		prod = shop_products.objects.all()
		serializer = shop_productsSerializer(prod , many=True)
		return Response(serializer.data)

	def post(self , request):
		pass


def Cart(request):
	cart_product = cart.objects.all()
	total_itm= len(cart_product)

	price = 0
	for i in cart_product:
		x=i.price
		price +=x

	return render(request,'cart.html',{'cart_itm':cart_product,'total_item':total_itm,'total_itm_price':price})


def add_to_cart(request, p_id):
	cart_product = shop_products.objects.filter(id=p_id)
	for itm in cart_product:
		name = itm.name
		price = itm.price
		img = itm.img
		category = itm.category
		desc  = itm.desc
		offer = itm.offer
	cart_data = cart(name=name,price=price,img=img,category=category,desc=desc,offer=offer)
	cart_data.save()
	return redirect('/shop')





def remove_from_cart(request,p_id):
	cart_product = cart.objects.filter(id=p_id).delete()
	return redirect('/shop/cart')








def checkout(request):
    if request.method =='POST':
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        street=request.POST['street']
        town_city=request.POST['town']
        pin=request.POST['postal']
        phone=request.POST['phone']
        email=request.POST['email']

        order_id = (f_name[-6:-1]+l_name[-6:-1]+pin[2:4]+email[6:6]+phone[:-6:-1])
        param_dict ={
            'MID':'ATEMPJ52617719243000',
            'ORDER_ID':order_id,
            'TXN_AMOUNT':'10',
            'CUST_ID':f_name,
            'EMAIL':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/'}
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        #print(param_dict['CHECKSUMHASH'])
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request,'checkout.html')
    


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
            print(response_dict['ORDERID'])
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            #print(response_dict['BANKNAME'])
            print(response_dict['ORDERID'])
            print(response_dict['TXNAMOUNT'])
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


def pageObject(request):
	#q = bla_bla_bla(bla_bla) 
    answer = request.GET['people_'] 
    print(answer)
    return render(request,'shop.html')