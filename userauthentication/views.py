from django.shortcuts import render


def loginPage(request):
    return render(request, "pages/login-page.html")
