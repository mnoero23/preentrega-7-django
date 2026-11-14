# Pruebas · Sitio profesional con Django

## Comandos obligatorios

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
```

## Cobertura automatizada

La suite contiene **20 pruebas**. Las 17 pruebas de la Pre-entrega 10 ya fueron aprobadas por Coderhouse y se agregaron 3 pruebas específicas para la recomendación de la profesora:

- Crear un artículo redirige al detalle y muestra el mensaje de éxito.
- Editar un artículo redirige al detalle y muestra el mensaje de éxito.
- Eliminar un artículo redirige al listado y muestra el mensaje de éxito.

También se valida:

- Registro y configuración de la app `posts`.
- Portada, perfil, navegación y archivos static.
- Modelo `Post` y listado de publicaciones.
- `PostForm` como `ModelForm` con campo `imagen`.
- Creación de un post con imagen.
- Carga mediante `multipart/form-data`.
- Edición del registro existente.
- Confirmación previa y eliminación únicamente mediante `POST`.
- Conservación de las pruebas de pre-entregas anteriores.

## Resultado esperado

- `System check identified no issues`.
- `No changes detected`.
- `Ran 20 tests`.
- `OK`.

## Prueba manual de aceptación

1. Ejecutar `python manage.py migrate` y `python manage.py runserver`.
2. Revisar la portada profesional, `/proyectos/` y `/acerca/`.
3. Abrir `/posts/crear/` y crear un artículo publicado con imagen.
4. Confirmar que el sitio redirige al detalle y muestra el mensaje de creación.
5. Confirmar que el artículo aparece en `/posts/` y que la imagen se ve correctamente.
6. Editar el artículo, cambiar la imagen y comprobar el mensaje de actualización.
7. Crear otro artículo sin imagen y comprobar que la página no se rompe.
8. Abrir la eliminación y verificar que primero aparezca la confirmación.
9. Confirmar el borrado y comprobar la redirección al listado y el mensaje final.
10. Revisar la versión móvil desde las herramientas del navegador.
