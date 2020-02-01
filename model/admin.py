from django.contrib import admin
from .models import User
from .models import Pais
from .models import Delegacion
from .models import Entrenador
from .models import Deporte
from .models import Ciudad
from .models import Deportista

# Register your models here.
admin.site.register(User)
admin.site.register(Pais)
admin.site.register(Delegacion)
admin.site.register(Deporte)
admin.site.register(Ciudad)
admin.site.register(Deportista)

