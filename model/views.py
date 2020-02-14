import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Deportista
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

# Create your views here.
from .serializers import DeportistaSerializer


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


@csrf_exempt
def get_sportsman_info(request):
    if request.method == 'GET':
        idDeportista = 10;
        print(idDeportista)
        #queryset = Deportista.objects.filter(idDeportista=idDeportista)
        queryset = Deportista.objects.select_related('idLugarNacimiento').filter(idDeportista=idDeportista)
        print(queryset)
        #serializer_class = DeportistaSerializer(queryset, many=True)
        data=serializers.serialize('json', queryset)
        #dump = json.dumps(queryset)
        return HttpResponse(data, content_type='application/json')


class StudentViewSet(viewsets.ModelViewSet):
    idDeportista = 10
    print(idDeportista)
    queryset = Deportista.objects.filter(idDeportista=idDeportista)
    serializer_class = DeportistaSerializer


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            do_login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o contraseña incorrectos'

    return JsonResponse({"message": message})


def login_user(request):
    return render(request, "deportistas/deportistas_list.html")


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
