from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('contact/', views.contact_us, name='contact_us'),
    path('shop/', views.shop, name='shop'),
]