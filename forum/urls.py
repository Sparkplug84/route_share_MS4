from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('<int:post_id>/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
