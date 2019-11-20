from rest_framework import serializers

from . models import Men_Collection

class Men_CollectionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Men_Collection
		fields = "__all__"
		


