from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.location_list, name='location-list'),
    path('locations/<int:pk>/', views.location_detail, name='location-detail'),
]