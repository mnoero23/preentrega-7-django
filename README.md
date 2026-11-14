# Matías Noero · Portfolio profesional con Python y Django

Sitio profesional de **Matías Noero** para presentar experiencia, proyectos y artículos, y demostrar de manera concreta conocimientos de Python y Django.

El proyecto nació como blog académico del curso de Python de Coderhouse y evoluciona como una base reutilizable para contenidos de LinkedIn, GitHub y el portfolio de **MN8**.

## Funcionalidades

- Portada y perfil profesional de Matías Noero.
- Sección de proyectos: ALQIVO, Faro Finanzas y Bitácora de Datos.
- Artículos persistidos en SQLite mediante el modelo `Post`.
- CRUD completo: listar, ver, crear, editar y eliminar.
- Confirmación previa al borrado.
- Mensajes de éxito después de crear, editar o eliminar.
- Imágenes opcionales mediante `ImageField` y Pillow.
- Formularios basados en `ModelForm`.
- Diseño responsive con templates heredados y CSS propio.
- Panel de administración.
- Pruebas automatizadas.

## Requisitos

- Python 3.12 o superior.
- Django 5.2.12.
- Pillow 12.0.0.

Las versiones utilizadas están declaradas en `requirements.txt`.

## Instalación limpia en Windows

Clonar el repositorio y entrar al proyecto:

```powershell
git clone https://github.com/mnoero23/mn8-portfolio-django.git
cd mn8-portfolio-django
```

Crear y activar un entorno virtual nuevo:

```powershell
py -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Instalar todas las dependencias, incluida Pillow:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Aplicar las migraciones es un paso obligatorio antes de ejecutar el sitio:

```powershell
python manage.py migrate
```

## Verificación y ejecución

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

El resultado esperado de `check` es `System check identified no issues`. La comprobación de migraciones debe indicar `No changes detected` y todos los tests deben finalizar con `OK`.

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

## Flujo del CRUD

- **Crear:** guarda el artículo y redirige a su detalle con un mensaje de éxito.
- **Leer:** permite listar artículos publicados y abrir su detalle.
- **Editar:** actualiza contenido e imagen y vuelve al detalle con confirmación.
- **Eliminar:** exige una pantalla de confirmación y redirige al listado con un mensaje de éxito.

## Manejo de imágenes

1. `Post.imagen` utiliza `ImageField(upload_to="posts/", null=True, blank=True)`.
2. Pillow está incluido en `requirements.txt`.
3. `MEDIA_ROOT` apunta a `media/` y `MEDIA_URL` a `/media/`.
4. El archivo principal de URLs sirve media solamente cuando `DEBUG=True`.
5. `PostForm` incluye el campo `imagen`.
6. Las vistas procesan `request.FILES` tanto al crear como al editar.
7. El formulario HTML usa `enctype="multipart/form-data"`.
8. Los templates verifican `{% if post.imagen %}` antes de acceder a la URL.

Para probar el flujo:

1. Entrar en `/posts/crear/`.
2. Crear un artículo con imagen JPG o PNG y estado **Publicado**.
3. Confirmar que la imagen aparezca en el listado y el detalle.
4. Editar el artículo y reemplazar la imagen.
5. Crear también un artículo sin imagen para comprobar que el template no se rompa.
6. Eliminar un artículo de prueba y verificar la confirmación previa y el mensaje final.

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

## Criterio de trabajo

Los próximos avances se organizarán en commits pequeños y descriptivos, separados por responsabilidad: modelo y migraciones, formularios, vistas, templates, pruebas y documentación.

`venv/`, `db.sqlite3`, `media/` y variables privadas están excluidos mediante `.gitignore`.
