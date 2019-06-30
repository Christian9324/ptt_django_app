# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .serializers import CreateSerializer
from rest_framework.generics import (CreateAPIView)
from rest_framework.views import APIView
from mapa.models import Post
from django.shortcuts import render

class PostCreateAPIView(CreateAPIView):
	serializer_class = CreateSerializer
	queryset = Post.objects.all()

def lista_ubicaciones(request):
	posts = Post.objects.all()
	return render(request, 'mapa/lista_ubicaciones.html', {'posts' : posts} )