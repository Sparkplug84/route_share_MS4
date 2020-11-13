from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_routes, name='routes'),
    path('<int:route_id>/', views.route_detail, name='route_detail'),
    path('add/', views.add_route, name='add_route'),
    path('edit/<int:route_id>/', views.edit_route, name='edit_route'),
]
