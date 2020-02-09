import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Deportista
from django.core.paginator import Paginator
# Create your views here.


def register(request):
    return render(request, 'Register/register.html', {})


def login(request):
    return render(request, 'Login/login.html', {})


def deportes_list(request):
    deportistas = Deportista.objects.select_related('idModalidadDeporte__idDeporte')
    paginator = Paginator(deportistas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if page_number is None:
        page_number = 1
    context = {
        'page': page_number,
        'deportistas': page_obj,
    }
    print(context)
    return render(request, 'deportistas/deportistas_list.html', context)


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))

