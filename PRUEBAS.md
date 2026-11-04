# Pruebas · Pre-entrega 9

## Comandos ejecutados

```powershell
python manage.py check
python manage.py test -v 2
```

## Resultado

- `System check identified no issues`.
- 11 pruebas ejecutadas correctamente.
- Inicio responde `200` y utiliza `posts/inicio.html`.
- Acerca de responde `200` y utiliza `posts/acerca.html`.
- La navegación está presente en las dos páginas.
- Django localiza `posts/css/estilos.css`.
- El HTML enlaza correctamente el archivo CSS.
- Se conservan las 3 verificaciones de configuración de la Pre-entrega 7.
- El modelo usa borrador como estado inicial y `__str__` devuelve el título.
- El listado muestra solamente posts publicados.
- Los posts se ordenan del más reciente al más antiguo.

## Prueba manual sugerida

1. Ejecutar `python manage.py runserver`.
2. Abrir `http://127.0.0.1:8000/`.
3. Verificar que el diseño tenga colores, tarjetas y tipografía aplicada.
4. Crear un superusuario e ingresar a `/admin/`.
5. Crear al menos tres posts con diferentes estados.
6. Abrir `/posts/` y confirmar que solo aparecen los publicados.
7. Confirmar que `estilos.css` responde con estado `200`.
