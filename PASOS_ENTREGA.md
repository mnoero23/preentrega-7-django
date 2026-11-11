# Pasos para revisar y entregar la Pre-entrega 10

## 1. Actualizar la copia local

```powershell
cd "C:\Users\matias\OneDrive\PERSONAL\01. CURSOS\02 - CODERHOUSE\2026 - Python\Modulo 6 - Git GitHub e introduccion a Django\07 - Preentrega 7"
git pull origin main
```

## 2. Preparar el entorno

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

Si el entorno virtual fue creado con otra instalación de Python y no funciona, recrearlo:

```powershell
deactivate
Rename-Item venv venv_anterior
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 3. Verificar

```powershell
python manage.py check
python manage.py test -v 2
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` y seguir la prueba manual de `PRUEBAS.md`.

## 4. Confirmar los cambios de Git

```powershell
git status
git log --oneline -3
```

## 5. Entregar

Cuando la revisión visual esté aprobada y los cambios estén publicados, pegar en Coderhouse:

`https://github.com/mnoero23/preentrega-7-django`
