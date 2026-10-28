# Pruebas · Pre-entrega 8

## Comandos ejecutados

```powershell
python manage.py check
python manage.py test -v 2
```

## Resultado

- `System check identified no issues`.
- 8 pruebas ejecutadas correctamente.
- Inicio responde `200` y utiliza `posts/inicio.html`.
- Acerca de responde `200` y utiliza `posts/acerca.html`.
- La navegación está presente en las dos páginas.
- Django localiza `posts/css/estilos.css`.
- El HTML enlaza correctamente el archivo CSS.
- Se conservan las 3 verificaciones de configuración de la Pre-entrega 7.

## Prueba manual sugerida

1. Ejecutar `python manage.py runserver`.
2. Abrir `http://127.0.0.1:8000/`.
3. Verificar que el diseño tenga colores, tarjetas y tipografía aplicada.
4. Navegar a «Acerca de» y volver a «Inicio».
5. Confirmar que `estilos.css` responde con estado `200`.
