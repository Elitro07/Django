from django.contrib import admin
from django.urls import path
from mainPDV import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainFunc, name='main'),
    path('register/', views.RegFunc, name='register'),
    path('login/', views.LoginFunc, name='login'),
    path('logout/', views.LogoutFunc, name='logout'),
]