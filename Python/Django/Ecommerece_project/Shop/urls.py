
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
	path('', views.Home , name='index'),
	path('about/',views.About , name='about'),
	path('cart/',views.Cart , name='cart'),
	path('shop/',views.Shop , name='shop'),
	path('shop/Collection_api/',views.Collection_api.as_view() , name='Collection_api'),
	
	path('shop/mens/', views.men_collection, name='men_collection') ,
	path('shop/womens/',views.women_collection, name='women_collection') ,
	path('shop/others/',views.other_collection, name='women_collection') ,
	path('shop/cloths/',views.cloth_collection, name='women_collection') ,
	path('shop/acs/',views.acs_collection, name='women_collection') ,
	path('shop/view-prod-item/<int:p_id>/',views.prod_review, name='product_review'),


	path('shop/cart/',views.Cart , name='cart'),
	path('cart/add-to-cart/<int:p_id>' , views.add_to_cart , name='add-to-cart'),
	path('cart/remove-from-cart/<int:p_id>', views.remove_from_cart , name='delete-cart-itm'),

	path('shop/checkout/',views.checkout , name='check-out'),
	
	path('shop/handlerequest/',views.handlerequest, name='catch_response'),
	path('blog/',views.Blog , name='blog'),
	path('single_blog/', views.Single_blog , name='single_blog'),
	path('shop/single_product/', views.Single_product , name='single_product'),
	path('contact/', views.Contact , name='contact'),
	path('acount/login/', views.Login , name='login'),
	path('acount/new_acount/', views.New_acount , name='new_acount'),
	path('acount/logout/', views.Logout, name='Logout'),

	path('pageObject/',views.pageObject ,name="pageObject")
   
	
]
