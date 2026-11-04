# Pasos para entregar la Pre-entrega 9

## 1. Actualizar la copia local

```powershell
git pull origin main
```

## 2. Preparar el entorno

```powershell
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 3. Verificar

```powershell
python manage.py check
python manage.py test -v 2
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Crear al menos tres publicaciones desde `http://127.0.0.1:8000/admin/` y comprobar que los posts publicados aparezcan en `http://127.0.0.1:8000/posts/`.

## 4. Confirmar Git

```powershell
git status
git log --oneline -3
```

El commit solicitado es `Checkpoint: Modelos y Admin configurados`.

## 5. Entregar

Pegar en Coderhouse la URL pública `https://github.com/mnoero23/preentrega-7-django`.
