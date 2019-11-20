
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [

	path('', views.Home , name='index'),
	path('about/', views.About , name='about'),
	path('cart/', views.Cart , name='cart'),
	path('shop/', views.Shop , name='shop'),
	path('shop/Collection_api/',views.Collection_api.as_view() , name='Collection_api'),
	path('shop/mens/' , views.men_collection, name='men_collection') ,
	path('shop/cart/', views.Cart , name='cart'),
	path('shop/checkout/', views.Checkout , name='check-out'),
	path('shop/blog/', views.Blog , name='blog'),
	path('single_blog/', views.Single_blog , name='single_blog'),
	path('shop/single_product/', views.Single_product , name='single_product'),
	path('contact/', views.Contact , name='contact'),
	path('account/login/', views.Login , name='login'),
	path('account/new_account/', views.New_account , name='new_account')

   
	
]
