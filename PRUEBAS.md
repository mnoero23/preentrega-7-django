# Pruebas · Pre-entrega 10

## Comandos ejecutados

```powershell
python manage.py check
python manage.py test -v 2
python manage.py makemigrations --check --dry-run
```

## Resultado automático

- `System check identified no issues`.
- **17 pruebas ejecutadas correctamente**.
- No hay cambios de modelo pendientes de migración.
- El modelo `Post` acepta una imagen opcional.
- `PostForm` es un `ModelForm` vinculado a `Post` e incluye `imagen`.
- El flujo permite crear un post con imagen.
- El detalle muestra título, autor y contenido.
- La edición actualiza el registro existente.
- El borrado requiere confirmación y solo se ejecuta mediante `POST`.
- El formulario HTML utiliza `multipart/form-data`.
- Se conservan las pruebas de las pre-entregas anteriores.

## Prueba manual recomendada

1. Ejecutar `python manage.py migrate` y `python manage.py runserver`.
2. Revisar la portada profesional, `/proyectos/` y `/acerca/`.
3. Abrir `/posts/crear/` y crear un artículo publicado con imagen.
4. Confirmar que aparece en `/posts/` y que la imagen se ve en el detalle.
5. Editar el artículo, cambiar la imagen y guardar.
6. Crear otro artículo sin imagen y comprobar que la página no se rompe.
7. Abrir la eliminación, cancelar y verificar que el post sigue existiendo.
8. Volver a eliminarlo y confirmar la operación.
9. Revisar la versión móvil desde las herramientas del navegador.
