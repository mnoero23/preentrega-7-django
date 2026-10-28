from django.apps import apps
from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class ConfiguracionInicialTest(SimpleTestCase):
    """Comprueba los requisitos de configuración de la Pre-entrega 7."""

    def test_app_posts_esta_registrada(self):
        self.assertEqual(apps.get_app_config("posts").name, "posts")

    def test_idioma_es_espanol_de_argentina(self):
        self.assertEqual(settings.LANGUAGE_CODE, "es-ar")

    def test_zona_horaria_es_buenos_aires(self):
        self.assertEqual(settings.TIME_ZONE, "America/Argentina/Buenos_Aires")


class SitioWebTest(SimpleTestCase):
    """Comprueba los requisitos funcionales de la Pre-entrega 8."""

    def test_inicio_responde_y_usa_su_template(self):
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "posts/inicio.html")
        self.assertContains(respuesta, "Bienvenido a Bitácora de Datos")

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
                self.assertContains(respuesta, reverse("posts:acerca"))

    def test_css_se_encuentra_en_static(self):
        self.assertIsNotNone(finders.find("posts/css/estilos.css"))

    def test_css_esta_vinculado_en_el_html(self):
        respuesta = self.client.get(reverse("posts:inicio"))
        self.assertContains(respuesta, "/static/posts/css/estilos.css")
