from .models import Comentario
from bootstrap_modal_forms.forms import BSModalForm


class VideoCommentForm(BSModalForm):
    class Meta:
        model = Comentario
        fields = ['idComentario', 'texto', 'usuario', 'participacion']
