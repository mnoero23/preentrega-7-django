# Pasos para entregar la Pre-entrega 8

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
python manage.py runserver
```

Comprobar `http://127.0.0.1:8000/` y `http://127.0.0.1:8000/acerca/`.

## 4. Confirmar Git

```powershell
git status
git log --oneline -3
```

## 5. Entregar

Pegar en Coderhouse la URL pública `https://github.com/mnoero23/preentrega-7-django`.
