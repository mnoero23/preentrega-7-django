import base64
import shutil
import tempfile

from django.apps import apps
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from .models import Post


class ConfiguracionInicialTest(SimpleTestCase):
    """Comprueba los requisitos de configuración de la Pre-entrega 7."""

    def test_app_posts_esta_registrada(self):
        self.assertEqual(apps.get_app_config("posts").name, "posts")

    def test_idioma_es_espanol_de_argentina(self):
        self.assertEqual(settings.LANGUAGE_CODE, "es-ar")

    def test_zona_horaria_es_buenos_aires(self):
        self.assertEqual(settings.TIME_ZONE, "America/Argentina/Buenos_Aires")


class SitioWebTest(TestCase):
    """Comprueba los requisitos funcionales de la Pre-entrega 8."""

    def test_inicio_responde_y_usa_su_template(self):
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "posts/inicio.html")
        self.assertContains(respuesta, "Convierto información y procesos")

    def test_acerca_responde_y_usa_su_template(self):
        respuesta = self.client.get(reverse("posts:acerca"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "posts/acerca.html")
        self.assertContains(respuesta, "Hola, soy Matías")

    def test_navegacion_esta_disponible_en_ambas_paginas(self):
        for nombre_url in ("posts:inicio", "posts:acerca"):
            with self.subTest(url=nombre_url):
                respuesta = self.client.get(reverse(nombre_url))
                self.assertContains(respuesta, reverse("posts:inicio"))
                self.assertContains(respuesta, reverse("posts:lista_posts"))
                self.assertContains(respuesta, reverse("posts:proyectos"))
                self.assertContains(respuesta, reverse("posts:acerca"))

    def test_css_se_encuentra_en_static(self):
        self.assertIsNotNone(finders.find("posts/css/estilos.css"))

    def test_css_esta_vinculado_en_el_html(self):
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertContains(respuesta, "/static/posts/css/estilos.css")


class PostModelTest(TestCase):
    """Comprueba el modelo y el listado dinámico de la Pre-entrega 9."""

    def test_post_tiene_valores_y_representacion_esperados(self):
        post = Post.objects.create(
            titulo="Mi primer post",
            contenido="Contenido de prueba",
            autor="Matías",
        )
        self.assertEqual(post.estado, Post.BORRADOR)
        self.assertEqual(str(post), "Mi primer post")

    def test_listado_muestra_solo_posts_publicados(self):
        publicado = Post.objects.create(
            titulo="Post visible",
            contenido="Se debe mostrar",
            autor="Matías",
            estado=Post.PUBLICADO,
        )
        borrador = Post.objects.create(
            titulo="Post oculto",
            contenido="No se debe mostrar",
            autor="Matías",
        )

        respuesta = self.client.get(reverse("posts:lista_posts"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "posts/lista_posts.html")
        self.assertContains(respuesta, publicado.titulo)
        self.assertNotContains(respuesta, borrador.titulo)

    def test_listado_respeta_orden_descendente(self):
        antiguo = Post.objects.create(
            titulo="Post antiguo",
            contenido="Primero creado",
            autor="Matías",
            estado=Post.PUBLICADO,
        )
        reciente = Post.objects.create(
            titulo="Post reciente",
            contenido="Último creado",
            autor="Matías",
            estado=Post.PUBLICADO,
        )

        respuesta = self.client.get(reverse("posts:lista_posts"))

        self.assertQuerySetEqual(
            respuesta.context["posts"],
            [reciente, antiguo],
        )


MEDIA_TEMPORAL = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_TEMPORAL)
class PostCrudTest(TestCase):
    """Valida el CRUD y el manejo de imágenes de la Pre-entrega 10."""

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_TEMPORAL, ignore_errors=True)

    def setUp(self):
        self.post = Post.objects.create(
            titulo="Automatización con Python",
            contenido="Un caso concreto de mejora de procesos.",
            autor="Matías Noero",
            estado=Post.PUBLICADO,
        )

    def test_formulario_es_model_form_y_contiene_imagen(self):
        from .forms import PostForm

        self.assertEqual(PostForm._meta.model, Post)
        self.assertIn("imagen", PostForm._meta.fields)

    def test_detalle_muestra_datos_del_post(self):
        respuesta = self.client.get(reverse("posts:detalle_post", args=[self.post.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, self.post.titulo)
        self.assertContains(respuesta, self.post.autor)

    def test_crear_post_con_imagen(self):
        png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
        )
        imagen = SimpleUploadedFile("prueba.png", png, content_type="image/png")
        respuesta = self.client.post(
            reverse("posts:crear_post"),
            {
                "titulo": "Proyecto con Django",
                "contenido": "Desarrollo completo.",
                "autor": "Matías Noero",
                "estado": Post.PUBLICADO,
                "imagen": imagen,
            },
        )
        creado = Post.objects.get(titulo="Proyecto con Django")
        self.assertRedirects(respuesta, reverse("posts:detalle_post", args=[creado.pk]))
        self.assertTrue(creado.imagen.name.startswith("posts/"))

    def test_editar_post(self):
        respuesta = self.client.post(
            reverse("posts:editar_post", args=[self.post.pk]),
            {
                "titulo": "Automatización mejorada",
                "contenido": self.post.contenido,
                "autor": self.post.autor,
                "estado": Post.PUBLICADO,
            },
        )
        self.post.refresh_from_db()
        self.assertRedirects(respuesta, reverse("posts:detalle_post", args=[self.post.pk]))
        self.assertEqual(self.post.titulo, "Automatización mejorada")

    def test_eliminar_requiere_confirmacion_post(self):
        url = reverse("posts:eliminar_post", args=[self.post.pk])
        respuesta_get = self.client.get(url)
        self.assertEqual(respuesta_get.status_code, 200)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

        respuesta_post = self.client.post(url)
        self.assertRedirects(respuesta_post, reverse("posts:lista_posts"))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_formulario_html_usa_multipart(self):
        respuesta = self.client.get(reverse("posts:crear_post"))
        self.assertContains(respuesta, 'enctype="multipart/form-data"')


    def test_crear_post_muestra_mensaje_de_exito(self):
        respuesta = self.client.post(
            reverse("posts:crear_post"),
            {
                "titulo": "Artículo nuevo",
                "contenido": "Contenido del artículo.",
                "autor": "Matías Noero",
                "estado": Post.PUBLICADO,
            },
            follow=True,
        )

        self.assertContains(respuesta, "La publicación se creó correctamente.")
        self.assertEqual(respuesta.resolver_match.url_name, "detalle_post")

    def test_editar_post_muestra_mensaje_de_exito(self):
        respuesta = self.client.post(
            reverse("posts:editar_post", args=[self.post.pk]),
            {
                "titulo": "Artículo actualizado",
                "contenido": self.post.contenido,
                "autor": self.post.autor,
                "estado": Post.PUBLICADO,
            },
            follow=True,
        )

        self.assertContains(respuesta, "La publicación se actualizó correctamente.")
        self.assertEqual(respuesta.resolver_match.url_name, "detalle_post")

    def test_eliminar_post_muestra_mensaje_de_exito(self):
        respuesta = self.client.post(
            reverse("posts:eliminar_post", args=[self.post.pk]),
            follow=True,
        )

        self.assertContains(respuesta, "La publicación se eliminó correctamente.")
        self.assertEqual(respuesta.resolver_match.url_name, "lista_posts")
