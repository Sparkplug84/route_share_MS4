from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_routes, name='routes'),
    path('<int:route_id>/', views.route_detail, name='route_detail'),
    path('add/', views.add_route, name='add_route'),
    path('add_instructions/', views.add_instructions, name='add_instructions'),
    path('edit/<int:route_id>/', views.edit_route, name='edit_route'),
    path('delete/<int:route_id>/', views.delete_route, name='delete_route'),
]
