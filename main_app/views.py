from django.shortcuts import render

def homePage(request):
    return render(request, "pages/index.html")

def login_page(request):
    return render(request, "pages/login-page.html")

def contact_us(request):
    return render(request, "pages/contact.html")

def add_product(request):
    return render(request, "pages/shop.html")