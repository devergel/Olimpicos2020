from django.shortcuts import render
from .models import Deportista
from django.core.paginator import Paginator
# Create your views here.


def register(request):
    return render(request, 'Register/register.html', {})


def login(request):
    return render(request, 'Login/login.html', {})


def deportes_list(request):
    deportesPrueba = Deportista.objects.select_related('idModalidadDeporte__idDeporte')
    paginator = Paginator(deportesPrueba, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if page_number is None:
        page_number = 1
    context = {
        'deportes'
        'page': page_number,
        'deportistas': page_obj,
    }
    print(context)
    return render(request, 'deportistas/deportistas_list.html', context)
