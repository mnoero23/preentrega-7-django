from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase


class ConfiguracionInicialTest(SimpleTestCase):
    """Comprueba los requisitos de configuración de la Pre-entrega 7."""

    def test_app_posts_esta_registrada(self):
        self.assertEqual(apps.get_app_config("posts").name, "posts")

    def test_idioma_es_espanol_de_argentina(self):
        self.assertEqual(settings.LANGUAGE_CODE, "es-ar")

    def test_zona_horaria_es_buenos_aires(self):
        self.assertEqual(settings.TIME_ZONE, "America/Argentina/Buenos_Aires")
