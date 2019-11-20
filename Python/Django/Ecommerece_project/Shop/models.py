from django.db import models

# Create your models here.


class New_prod_arrival(models.Model):
	prod_id = models.AutoField(primary_key = True)
	prodd_img = models.ImageField(upload_to='pics')
	prod_category = models.CharField(max_length=40)
	prod_name = models.CharField(max_length=100)
	prod_price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.prod_name



class Flash_latest_prod(models.Model):
	
	prod_img = models.ImageField(upload_to='pics')
	prod_title = models.CharField(max_length=50)
	prod_desc = models.TextField(max_length=200)



class Men_Collection(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.name


class Women_Collection(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.name



class Accesories(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.name


class Clothing(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()

	def __str__(self):
		return self.name

class Other(models.Model):
	img = models.ImageField(upload_to='pics')
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	desc  = models.TextField(max_length=500)
	price = models.IntegerField()
	offer = models.BooleanField()
	def __str__(self):
		return self.name






	
