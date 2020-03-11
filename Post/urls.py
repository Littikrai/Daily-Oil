from django.urls import path
from . import views
urlpatterns = [
    path('', views.post, name='post'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('updates/<int:post_id>/', views.updates, name='updates'),
    path('updates/<int:post_id><str:status>/', views.hide_post, name='hide')
]