# Blog Project · Pre-entrega 7

Base inicial de un blog web desarrollado con Django para el curso de Python de Coderhouse. En este checkpoint se configura el proyecto `blog_project` y la aplicación principal `posts`. Los modelos, vistas, templates y funcionalidades del blog se incorporarán en las próximas entregas.

## Requisitos

- Python 3.10 o superior.
- Git.

## Clonar el repositorio

```powershell
git clone https://github.com/mnoero23/preentrega-7-django.git
cd preentrega-7-django
```

## Crear y activar el entorno virtual

En Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

## Verificar la configuración

```powershell
python manage.py check
```

El resultado esperado es `System check identified no issues`.

## Ejecutar el servidor

```powershell
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador. Para detener el servidor, presionar `Ctrl+C`.

## Estructura principal

```text
preentrega-7-django/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── posts/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

## Configuración aplicada

- Proyecto Django: `blog_project`.
- Aplicación principal: `posts`.
- Registro en `INSTALLED_APPS`: `posts.apps.PostsConfig`.
- Idioma: español de Argentina (`es-ar`).
- Zona horaria: `America/Argentina/Buenos_Aires`.
- Base de datos local `db.sqlite3` excluida de Git.
- Entornos virtuales y variables privadas excluidos mediante `.gitignore`.

## Alcance del checkpoint

Esta entrega prepara únicamente la base técnica. Todavía no incluye modelos propios, vistas, templates, formularios, rutas de `posts`, CRUD, autenticación, estilos personalizados ni carga de imágenes.
