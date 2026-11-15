# 600 kits para crear

Sitio bilingue de Creative Commons Venezuela para documentar el primer ciclo del programa de kits educativos en Caracas y La Guaira.

Live at: **https://venezuela-org.github.io/donate/**

## Estado publicado — 15 de noviembre de 2026

- 600 kits armados
- 600 kits entregados (100%)
- Más de 60 dibujos recibidos mediante los QR
- Últimos 91 kits entregados en Caraballeda el 14 de noviembre
- Entregas verificadas: 325 en La Guaira (3 de octubre), 184 en Caracas (8 de octubre) y 91 en Caraballeda (14 de noviembre)
- US$2.800 recaudados
- 84% compras, 5% comisiones y cambio, 2% logistica, 9% reservado para premios
- Cierre del concurso: 30 de noviembre de 2026
- El portal para recibir dibujos permanece abierto permanentemente

## Publicacion

Es un sitio estatico sin dependencias ni proceso de compilacion. GitHub Pages publica directamente `index.html`.

```bash
git add .
git commit -m "Complete first cycle: 600 kits delivered"
git push origin main
```

## Vista local

```bash
python3 -m http.server 8000
```

Abrir:

- Ingles: `http://localhost:8000/`
- Espanol: `http://localhost:8000/?lang=es`

## Archivos principales

- `index.html`: pagina completa, estilos, textos bilingues y selector de idioma.
- `status-600-delivered-es.png` / `status-600-delivered-en.png`: afiches finales de estado.
- `chronology-es.png` / `chronology-en.png`: cronologia visual.
- `docs/cronologia-y-plan-tecnico.md`: cronologia ampliada y plan de continuidad.
- `gallery.html`, `gallery.css`, `gallery.js`, `drawings.json`: prototipo bilingue de la galeria publica.
- `docs/gallery-data-spec.md`: separacion entre datos publicos y el registro privado de evidencias.

Para una futura actualizacion, cambiar juntos los indicadores del encabezado, el progreso de entregas, la fecha del pie y los afiches correspondientes.
