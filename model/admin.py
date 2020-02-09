from django.contrib import admin
from .models import Comentario
from .models import Participacion
from .models import Evento
from .models import ModadalidadDeporte
from .models import Deporte
from .models import Deportista
from .models import LugarNacimiento
from .models import Delegacion
from .models import Entrenador

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Participacion)
admin.site.register(Evento)
admin.site.register(ModadalidadDeporte)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(LugarNacimiento)
admin.site.register(Delegacion)
admin.site.register(Entrenador)
