import json

from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import VideoCommentForm
from .models import Deportista, Participacion, Comentario, Deporte, ModadalidadDeporte
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


def register(request):
    return render(request, 'Register/register.html', {})


def login(request):
    return render(request, 'Login/login.html', {})


def deportista_detail(request, id):
    print(id)
    context = {
        'id': id
    }
    return render(request, 'deportistas/deportista_detail.html', context)


def deportes_list(request):
    deportistas = Deportista.objects.select_related(
        'idModalidadDeporte__idDeporte')
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

        user_model = User.objects.create_user(
            username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def get_sportsman_info(request):
    if request.method == 'GET':
        idDeportista = request.GET.get('id')
        queryset = Deportista.objects.select_related().filter(idDeportista=idDeportista)
        data = []
        for deportista in queryset:
            data.append({
                'idDeportista': deportista.idDeportista,
                'nombre': deportista.nombre,
                'apellido': deportista.apellido,
                'edad': deportista.edad,
                'peso': str(deportista.peso),
                'estatura': str(deportista.estatura),
                'foto': deportista.foto.url.strip('model'),
                'fechanacimiento': str(deportista.fechaNacimiento),
                'ciudad': deportista.idLugarNacimiento.ciudad,
                'pais': deportista.idLugarNacimiento.pais,
                'nombreentrenador': deportista.idEntrenador.nombre,
                'apellidoentrenador': deportista.idEntrenador.apellido,
                'nombredelegacion': deportista.idDelegacion.nombre,
                'icono': deportista.idModalidadDeporte.idDeporte.icono.url.strip('model')
            })

        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')


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


@csrf_exempt
def get_info_participation(request):
    if request.method == 'GET':
        idDeportista = request.GET.get('id')

        queryset = Participacion.objects.select_related().filter(deportista_id=idDeportista)
        data = []
        for participacion in queryset:
            data.append({
                'idParticipacion': participacion.idParticipacion,
                'linkVideo': participacion.linkVideo,
                'deportista_id': participacion.deportista_id,
                'descripcion': participacion.modalidadDeporte.nombreModalidad,
                'fecha': str(participacion.evento.fecha),
                'resultado': participacion.resultado
            })

        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')


class VideoCommentView(BSModalCreateView):
    template_name = 'templates/deportistas/video_comment.html'
    form_class = VideoCommentForm
    success_message = 'Comentario creado Existosamente'
    success_url = reverse_lazy('deportista_detail')


@csrf_exempt
def add_comment(request):
    response = "Invalid Request"
    if request.method == 'POST' and request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)

        response = save_comment(request, response, user)

    if not request.user.is_authenticated:
        response = "Permision Denied"

    return JsonResponse({"message": response})


def save_comment(request, response, user):
    print(type(user))
    jsonUser = json.loads(request.body)
    texto = jsonUser['texto']
    participacion = jsonUser['participacion']
    comment_model = Comentario()
    comment_model.texto = texto
    comment_model.usuario = user
    comment_model.participacion = Participacion.objects.get(
        idParticipacion=participacion)
    comment_model.save()
    response = "ok"
    return response


def deportistas_list_service(request):
    if request.method == 'GET':
        deportistas = Deportista.objects.select_related(
            'idModalidadDeporte__idDeporte')
        data = []
        for deportista in deportistas:
            data.append({
                'idDeportista': deportista.idDeportista,
                'nombre': deportista.nombre,
                'apellido': deportista.apellido,
                'icono': deportista.idModalidadDeporte.idDeporte.icono.url.strip('model'),
                'foto': deportista.foto.url.strip('model'),
                'modalidadDeporte': deportista.idModalidadDeporte.nombreModalidad,
                'deporte': deportista.idModalidadDeporte.idDeporte.nombreDeporte

            })

        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')


def sport_service(request):
    if request.method == 'GET':
        deportes = Deporte.objects.select_related()
        data = []
        for deporte in deportes:
            data.append({
                'idDeporte': deporte.idDeporte,
                'nombreDeporte': deporte.nombreDeporte

            })

        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')


def mode_service(request):
    if request.method == 'GET':
        idDeporte = request.GET.get('idDeporte')
        modalidades = ModadalidadDeporte.objects.select_related().filter(idDeporte=idDeporte)
        data = []
        for modalidad in modalidades:
            data.append({
                'idModalidadDeporte': modalidad.idModalidadDeporte,
                'nombreModalidad': modalidad.nombreModalidad,
                'idDeporte': modalidad.idDeporte.idDeporte,
                'nombreDeporte': modalidad.idDeporte.nombreDeporte

            })
        print(data)
        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')


def comment_service(request):
    if request.method == 'GET':
        idParticipacion = request.GET.get('id')
        comentarios = Comentario.objects.select_related().filter(participacion_id=idParticipacion)
        data = []
        for comentario in comentarios:
            data.append({
                'id': idParticipacion,
                'texto': comentario.texto,
                'usuario': comentario.usuario.username
            })
        print(data)
        dataJson = json.dumps(data)
        return HttpResponse(dataJson, content_type='application/json')