from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from . Serializers import Men_CollectionSerializer
from rest_framework.response import Response
from django.core.paginator import Paginator






# Create your views here.

def Home(request):

	new_prod = New_prod_arrival.objects.all()
	flash_prod = Flash_latest_prod.objects.all()


	return render(request , 'home.html' , {'new_prod_arriaval': new_prod ,'flash_prods':flash_prod})



def About(request):
	return render(request , 'about.html')



def Shop(request):
	return render(request , 'shop.html')

def men_collection(request):

	men_collections = Men_Collection.objects.all()	

	paginator = Paginator(men_collections, 3) # Show 9 contacts per page
	page = request.GET.get('page')
	men_prods = paginator.get_page(page)

	# Number of page in Page
	num_page = paginator.page_range
	for i in num_page:
		print(i)


	return render(request , 'Men_collection.html' ,{'men_prod':men_prods ,'pages':num_page})


class Collection_api(APIView):

	def get(self , request):
		prod = Men_Collection.objects.all()
		serializer = Men_CollectionSerializer(prod , many=True)
		return Response(serializer.data)

	def post(self , request):
		pass





def Cart(request):
	return render(request , 'cart.html')



def Checkout(request):
	return render(request , 'checkout.html')



def Blog(request):
	return render(request , 'blog.html')



def Single_blog(request):
	return render(request , 'blog-single.html')



def Single_product(request):
	return render(request , 'product-single.html')



def Contact(request):
	return render(request, 'contact.html')



def Login(request):
	return render(request, 'login.html')




def New_account(request):
	return render(request, 'new_account.html')
