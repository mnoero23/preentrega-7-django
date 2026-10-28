from django.shortcuts import render


def inicio(request):
    """Muestra la portada del blog."""
    return render(request, "posts/inicio.html")


def acerca(request):
    """Presenta al autor y el propósito del proyecto."""
    return render(request, "posts/acerca.html")
