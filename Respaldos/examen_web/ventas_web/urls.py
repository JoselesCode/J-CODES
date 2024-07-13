from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cash-gta/', views.cash_gta, name='Cash_gta'),
    path('crud-empleado/', views.crud_empleado, name='crud_empleado'),
    path('formulario-contacto/', views.formulario_contacto, name='formulario_contacto'),
    path('fornite/', views.fornite, name='fornite'),
    path('index-login/', views.index_login, name='index_login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('rp-riot/', views.rp_riot, name='rp_riot'),
    path('signup/', views.signup, name='signup'),
]
