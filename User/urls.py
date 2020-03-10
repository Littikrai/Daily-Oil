from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('register/', views.add_user, name='register'),
    path('logout/', views.user_logout, name='logout')
]
