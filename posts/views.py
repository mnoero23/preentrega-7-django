from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


PROYECTOS = [
    {
        "nombre": "ALQIVO",
        "categoria": "Producto digital",
        "descripcion": "Plataforma para administrar alquileres, reservas, gastos, propietarios y la experiencia del huésped.",
        "tecnologias": "Next.js · Supabase · Datos",
    },
    {
        "nombre": "Faro Finanzas",
        "categoria": "Finanzas personales",
        "descripcion": "Herramienta para ordenar cuentas, inversiones y objetivos con una lectura clara de resultados y movimientos.",
        "tecnologias": "Análisis de datos · UX · Automatización",
    },
    {
        "nombre": "Bitácora de Datos",
        "categoria": "Python y Django",
        "descripcion": "Sitio profesional y laboratorio técnico para publicar aprendizajes y demostrar desarrollo web con Django.",
        "tecnologias": "Python · Django · SQLite",
    },
]


def inicio(request):
    """Muestra la portada profesional con contenido destacado."""
    destacados = Post.objects.filter(estado=Post.PUBLICADO)[:3]
    return render(
        request,
        "posts/inicio.html",
        {"destacados": destacados, "proyectos": PROYECTOS},
    )


def lista_posts(request):
    """Lista únicamente las publicaciones visibles del blog."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


def detalle_post(request, pk):
    """Muestra una publicación individual, incluida su imagen si existe."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


def crear_post(request):
    """Crea una publicación procesando datos y archivos."""
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save()
        messages.success(request, "La publicación se creó correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(request, "posts/post_form.html", {"form": form, "modo": "Crear"})


def editar_post(request, pk):
    """Actualiza una publicación existente y permite reemplazar su imagen."""
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and form.is_valid():
        post = form.save()
        messages.success(request, "La publicación se actualizó correctamente.")
        return redirect("posts:detalle_post", pk=post.pk)
    return render(
        request,
        "posts/post_form.html",
        {"form": form, "modo": "Editar", "post": post},
    )


def eliminar_post(request, pk):
    """Elimina una publicación únicamente después de una confirmación POST."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "La publicación se eliminó correctamente.")
        return redirect("posts:lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})


def proyectos(request):
    """Presenta una selección de proyectos de Matías y MN8."""
    return render(request, "posts/proyectos.html", {"proyectos": PROYECTOS})


def acerca(request):
    """Presenta al autor y el propósito del proyecto."""
    return render(request, "posts/acerca.html")
