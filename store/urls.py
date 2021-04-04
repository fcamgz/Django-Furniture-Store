from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('manage/', views.manage, name='manage'),
    path('furniture/', views.furniture, name='furniture'),
    path('contact/',views.contact, name='contact'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('create_furniture/', views.create_furniture, name='create_furniture'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_furniture/<str:name>/', views.update_furniture, name='update_furniture'),
    path('delete_furniture/<str:name>/', views.delete_furniture, name='delete_furniture'),
    path('update_order/<str:pk>/',views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
]