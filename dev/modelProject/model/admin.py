from django.contrib import admin
from .models import User
from .models import Pais
from .models import Delegacion
from .models import Entrenador

# Register your models here.
admin.site.register(User)
admin.site.register(Pais)
admin.site.register(Delegacion)
admin.site.register(Entrenador)

