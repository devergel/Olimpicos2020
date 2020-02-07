from django.shortcuts import render
from .models import Deportista
from django.core.paginator import Paginator
# Create your views here.


def register(request):
    return render(request, 'Register/register.html', {})


def login(request):
    return render(request, 'Login/login.html', {})


def deportes_list(request):
    list = Deportista.objects.all()
    paginator = Paginator(list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if page_number is None:
        page_number = 1
    context = {
        'page': page_number,
        'deportistas': page_obj,
        'deportes': ['Atletismo', 'Natacion', 'Futbol']
    }
    print(context)
    return render(request, 'deportistas/deportistas_list.html', context)
