# Bitácora de Datos · Pre-entrega 9

Blog desarrollado con Django para el curso de Python de Coderhouse. Esta entrega incorpora un modelo persistente, administración de contenido y consultas mediante el ORM sobre la interfaz construida anteriormente.

## Funcionalidades

- Página de inicio con bienvenida y presentación del proyecto.
- Página «Acerca de» con reseña del autor y propósito del sitio.
- Navegación mediante rutas con nombre.
- Layout reutilizable con herencia de templates.
- Diseño responsive mediante CSS servido desde `static/`.
- Pruebas automáticas de rutas, templates, navegación y CSS.
- Modelo `Post` con estados borrador, publicado y archivado.
- Migraciones de base de datos incluidas.
- Panel administrativo con filtros, búsqueda y columnas útiles.
- Listado dinámico que muestra únicamente posts publicados.

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

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) y comprobar la navegación hacia `/posts/`, `/acerca/` y `/admin/`.

## Panel administrativo

Crear un administrador local (las credenciales no se guardan en Git):

```powershell
python manage.py createsuperuser
python manage.py runserver
```

Ingresar en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) y crear al menos tres posts. Solo los que tengan estado **Publicado** aparecerán en `/posts/`.

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
    │   ├── lista_posts.html
    │   └── acerca.html
    ├── migrations/
    │   └── 0001_initial.py
    ├── admin.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Cómo funciona

1. `blog_project/urls.py` delega las rutas a `posts/urls.py` mediante `include()`.
2. `Post` representa las publicaciones y Django lo persiste en SQLite mediante migraciones.
3. `PostAdmin` permite gestionar el contenido desde `/admin/`.
4. `lista_posts` consulta posts publicados con el ORM y los envía al template.
5. Los templates hijos extienden `base.html`, que reúne estructura y navegación.
6. `base.html` carga `posts/css/estilos.css` mediante `{% load static %}`.

## Configuración

- Django 5.2.12.
- App `posts.apps.PostsConfig`.
- Idioma `es-ar` y zona horaria `America/Argentina/Buenos_Aires`.
- `venv/`, `db.sqlite3` y variables privadas excluidos mediante `.gitignore`.
