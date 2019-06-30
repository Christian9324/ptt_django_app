from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mapa.models import Post


class CreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'latitud',
			'longitud',
			]