from django.db import models

# create your models here


class Destination(models.Model):

	place = models.CharField(max_length=100)
	img = models.ImageField(upload_to='Pics')
	desc = models.TextField(max_length=500)
	price = models.IntegerField()



