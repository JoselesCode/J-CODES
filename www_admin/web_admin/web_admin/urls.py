"""web_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.urls import include  #  <<==========
from administrador import views   #  <<==========


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), 
    path('', views.index, name= "index"),
    path('listar', views.listar, name= "listar"),   
    path('agregar', views.agregar, name= "agregar"),   
    path('actualizar', views.actualizar, name= "actualizar"),   
    path('eliminar', views.eliminar, name= "eliminar"),
 
    path('listar2', views.listar2, name= "listar2"),   
    path('agregar2', views.agregar2, name= "agregar2"),   
    path('actualizar2', views.actualizar2, name= "actualizar2"),   
    path('eliminar2', views.eliminar2, name= "eliminar2"),

    path('indexF', views.indexF, name= "indexF"), 
    path('indexgta', views.indexgta, name= "indexgta"),
    path('indexform', views.indexform, name= "indexform"),
       
    ]
