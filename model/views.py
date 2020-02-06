from django.shortcuts import render
# Create your views here.
def register(request):
    return render(request, 'Register/register.html', {})


def login(request):
    return render(request, 'Login/login.html', {})