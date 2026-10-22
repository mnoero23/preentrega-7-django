# Evidencia de verificación

Se realizaron los siguientes controles:

```powershell
python manage.py check
python manage.py test
```

También se verificó que:

- `manage.py` esté en la raíz.
- `blog_project/settings.py` exista.
- la app `posts` esté creada y registrada como `posts.apps.PostsConfig`;
- el idioma sea `es-ar`;
- la zona horaria sea `America/Argentina/Buenos_Aires`;
- `.gitignore` excluya `venv/`, `.env` y `db.sqlite3`;
- `requirements.txt` incluya Django;
- el servidor de desarrollo responda correctamente.

Las tres pruebas automatizadas incluidas comprueban el registro de la app, el idioma y la zona horaria.
