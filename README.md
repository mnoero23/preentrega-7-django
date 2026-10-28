# Bitácora de Datos · Pre-entrega 8

Primera versión visual de un blog desarrollado con Django para el curso de Python de Coderhouse. Implementa el flujo **URL → view → template → archivo estático** y continúa sobre la base de la Pre-entrega 7.

## Funcionalidades

- Página de inicio con bienvenida y presentación del proyecto.
- Página «Acerca de» con reseña del autor y propósito del sitio.
- Navegación mediante rutas con nombre.
- Layout reutilizable con herencia de templates.
- Diseño responsive mediante CSS servido desde `static/`.
- Pruebas automáticas de rutas, templates, navegación y CSS.

## Instalación

```powershell
git clone https://github.com/mnoero23/preentrega-7-django.git
cd preentrega-7-django
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En Linux o macOS, activar el entorno con `source venv/bin/activate`.

## Verificación y ejecución

```powershell
python manage.py check
python manage.py test -v 2
python manage.py migrate
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) y comprobar la navegación hacia [http://127.0.0.1:8000/acerca/](http://127.0.0.1:8000/acerca/).

## Estructura principal

```text
preentrega-7-django/
├── manage.py
├── requirements.txt
├── README.md
├── blog_project/
│   ├── settings.py
│   └── urls.py
└── posts/
    ├── static/posts/css/
    │   └── estilos.css
    ├── templates/posts/
    │   ├── base.html
    │   ├── inicio.html
    │   └── acerca.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Cómo funciona

1. `blog_project/urls.py` delega las rutas a `posts/urls.py` mediante `include()`.
2. Las funciones `inicio` y `acerca` renderizan sus respectivos templates.
3. Los templates hijos extienden `base.html`, que reúne estructura y navegación.
4. `base.html` carga `posts/css/estilos.css` mediante `{% load static %}`.

## Configuración

- Django 5.2.12.
- App `posts.apps.PostsConfig`.
- Idioma `es-ar` y zona horaria `America/Argentina/Buenos_Aires`.
- `venv/`, `db.sqlite3` y variables privadas excluidos mediante `.gitignore`.
