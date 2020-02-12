
from django.urls import path

from . import views



urlpatterns = [

    path('', views.Index, name='Index'),
    path('about/', views.About, name='About'),
    path('services/', views.Services, name='Service'),
    path('news/', views.News, name='News'),
    path('contact/', views.Contact, name='Contact'),
    path('signup/', views.Sign_up, name='Sign_up'),
    path('login/', views.Login, name='login'),
    path('dashboard/', views.Dashboard, name='dash'),
    path('logout/', views.Logout,name="Logout")

   
    ]


