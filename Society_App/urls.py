from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('farmers/<int:pk>/', views.farmer_detail, name='farmer_detail'),
    path('farmers/register/', views.farmer_register, name='farmer_register'),
    path('farmers/<int:pk>/update/', views.farmer_update, name='farmer_update'),
    path('farmers/<int:pk>/delete/', views.farmer_delete, name='farmer_delete'),
]



