# Matías Noero · Sitio profesional con Django

Evolución del blog del curso de Python de Coderhouse. La **Pre-entrega 10** incorpora un CRUD completo de artículos con imágenes y convierte el proyecto en un pequeño sitio profesional: presentación, artículos, proyectos y demostración concreta de conocimientos en Python y Django.

El contenido está pensado para poder reutilizar aprendizajes y casos posteriormente en LinkedIn, GitHub y el portfolio de **MN8**.

## Funcionalidades

- Portada profesional de Matías Noero.
- Sección de proyectos con ALQIVO, Faro Finanzas y Bitácora de Datos.
- Página de perfil profesional.
- Artículos persistidos en SQLite mediante el modelo `Post`.
- CRUD desde la interfaz: listar, ver, crear, editar y eliminar.
- Confirmación previa al borrado.
- Imágenes opcionales mediante `ImageField` y Pillow.
- Formularios basados en `ModelForm`.
- Mensajes de confirmación después de crear, editar o eliminar.
- Diseño responsive con templates heredados y CSS propio.
- Panel de administración y pruebas automáticas.

## Instalación en Windows

```powershell
git clone https://github.com/mnoero23/preentrega-7-django.git
cd preentrega-7-django
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

## Verificación y ejecución

```powershell
python manage.py check
python manage.py test -v 2
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Rutas principales

| Ruta | Función |
|---|---|
| `/` | Portada profesional |
| `/posts/` | Listado de artículos publicados |
| `/posts/crear/` | Crear un artículo |
| `/posts/<id>/` | Ver el detalle |
| `/posts/<id>/editar/` | Editar el artículo y su imagen |
| `/posts/<id>/eliminar/` | Confirmar y eliminar |
| `/proyectos/` | Portfolio de proyectos |
| `/acerca/` | Perfil profesional |
| `/admin/` | Administración de Django |

## Manejo de imágenes

1. `Post.imagen` utiliza `ImageField(upload_to="posts/", null=True, blank=True)`.
2. Pillow está incluido en `requirements.txt`.
3. `MEDIA_ROOT` apunta a `media/` y `MEDIA_URL` a `/media/`.
4. El archivo principal de URLs sirve media cuando `DEBUG=True`.
5. `PostForm` incluye el campo `imagen`.
6. Las vistas reciben `request.FILES` al crear y editar.
7. El formulario HTML usa `enctype="multipart/form-data"`.
8. Los templates comprueban `{% if post.imagen %}` antes de acceder a su URL.

Para probarlo, crear un artículo desde `/posts/crear/`, seleccionar una imagen JPG o PNG, marcar el estado **Publicado** y guardar. La imagen aparecerá en el listado y en el detalle. También se puede crear un artículo sin imagen.

## Estructura relevante

```text
blog_project/
├── settings.py
└── urls.py
posts/
├── migrations/
│   ├── 0001_initial.py
│   └── 0002_post_imagen.py
├── static/posts/css/estilos.css
├── templates/posts/
│   ├── base.html
│   ├── inicio.html
│   ├── lista_posts.html
│   ├── detalle_post.html
│   ├── post_form.html
│   ├── post_confirm_delete.html
│   ├── proyectos.html
│   └── acerca.html
├── forms.py
├── models.py
├── urls.py
├── views.py
└── tests.py
```

## Dependencias

- Python 3.12 o superior.
- Django 5.2.12.
- Pillow 12.0.0.

`venv/`, `db.sqlite3`, `media/` y variables privadas están excluidos mediante `.gitignore`.
