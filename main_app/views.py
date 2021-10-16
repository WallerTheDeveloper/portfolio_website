from django.shortcuts import render, get_object_or_404
from .models import Book

def homePage(request):
    return render(request, "pages/index.html")

def login_page(request):
    return render(request, "pages/login-page.html")

def contact_us(request):
    return render(request, "pages/contact.html")

def shop(request):
    return render(request, "pages/shop.html")