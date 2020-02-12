from rest_framework import serializers

from . models import shop_products

class shop_productsSerializer(serializers.ModelSerializer):

	class Meta:
		model = shop_products
		fields = "__all__"
		


