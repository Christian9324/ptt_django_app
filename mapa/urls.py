from django.urls import path
from django.conf.urls import url, include
from mapa import views

urlpatterns = [
    url(r'^create/$', views.PostCreateAPIView.as_view()),
    path('', views.lista_ubicaciones , name='lista_ubicaciones'),
]