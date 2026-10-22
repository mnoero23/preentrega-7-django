# Pasos de publicación

## 1. Verificar el proyecto

Desde PowerShell, dentro de la carpeta que contiene `manage.py`:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python manage.py test -v 2
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` y detener el servidor con `Ctrl+C`.

## 2. Crear el repositorio

Crear en GitHub un repositorio público llamado `preentrega-7-django`, vacío: no agregar README, `.gitignore` ni licencia desde GitHub porque ya existen localmente.

## 3. Crear un historial claro

```powershell
git init
git branch -M main
git add manage.py blog_project posts
git commit -m "Inicializar proyecto Django y app posts"
git add .gitignore requirements.txt README.md PRUEBAS.md PASOS_ENTREGA.md
git commit -m "Configurar entorno y documentar ejecución"
git remote add origin https://github.com/mnoero23/preentrega-7-django.git
git push -u origin main
```

## 4. Comprobar y entregar

```powershell
git status
git log --oneline
```

Comprobar en GitHub que no aparezcan `venv/`, `.env`, `db.sqlite3` ni `__pycache__`. Entregar esta URL:

```text
https://github.com/mnoero23/preentrega-7-django
```
