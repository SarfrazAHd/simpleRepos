from django.db import models

# Create your models here.

class Flash_latest_prod(models.Model):
	
	prod_img = models.ImageField(upload_to='pics')
	prod_title = models.CharField(max_length=50)
	prod_desc = models.TextField(max_length=200)


class shop_products(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()
	def __str__(self):
		return self.name


class cart(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.name





class order(models.Model):
	firstName = models.CharField(max_length=50)
	laststName = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	town_city = models.CharField(max_length=50)
	postal = models.IntegerField()
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.firstName




	
