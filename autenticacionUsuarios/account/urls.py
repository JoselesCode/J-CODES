from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #path('login/', views.user_login, name='login')
    #path('login/', auth_views.LoginView.as_view(), name= 'login'),
    #path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name= 'Password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name= 'Password_change_done'),
    path('', include('django.contrib.auth.urls')), #con este llamo a todos los de arriba
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
]

