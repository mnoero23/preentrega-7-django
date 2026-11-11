from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Formulario del sitio para crear y actualizar publicaciones."""

    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"placeholder": "Ej.: Cómo transformé una necesidad en una app"}
            ),
            "contenido": forms.Textarea(
                attrs={"rows": 10, "placeholder": "Desarrollá la idea, el proceso y el aprendizaje..."}
            ),
            "autor": forms.TextInput(attrs={"placeholder": "Matías Noero"}),
        }

