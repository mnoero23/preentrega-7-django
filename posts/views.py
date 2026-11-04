from django.shortcuts import render

from .models import Post


def inicio(request):
    """Muestra la portada del blog."""
    return render(request, "posts/inicio.html")


def lista_posts(request):
    """Lista únicamente las publicaciones visibles del blog."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


def acerca(request):
    """Presenta al autor y el propósito del proyecto."""
    return render(request, "posts/acerca.html")
