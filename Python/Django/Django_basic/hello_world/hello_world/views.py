



from django.http import HttpResponse
from django.shortcuts import render




def index(request):
	return HttpResponse("<h1>Welcome to Django learning Phase from sarfraz ahmad</h1>")




def home(request):
	return render(request,'file.html')