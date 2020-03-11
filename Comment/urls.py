from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete/<int:post_id><int:comment_id>/', views.Delete_comment, name='delete')
]