# 600 kits para crear

Sitio bilingue de Creative Commons Venezuela para documentar el primer ciclo del programa de kits educativos en Caracas y La Guaira.

Live at: **https://venezuela-org.github.io/donate/**

## Estado publicado — 10 de octubre de 2026

- 600 kits armados
- 509 kits entregados
- 60 dibujos recibidos mediante los QR
- 91 kits pendientes de entrega
- US$2.800 recaudados
- 84% compras, 5% comisiones y cambio, 2% logistica, 9% reservado para premios
- Cierre del concurso: 30 de noviembre de 2026
- El portal para recibir dibujos permanece abierto permanentemente

## Publicacion

Es un sitio estatico sin dependencias ni proceso de compilacion. GitHub Pages publica directamente `index.html`.

```bash
git add .
git commit -m "Update project status: 600 assembled, 509 delivered"
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
- `status-509-delivered-es.png` / `status-509-delivered-en.png`: afiches de estado.
- `chronology-es.png` / `chronology-en.png`: cronologia visual.
- `docs/cronologia-y-plan-tecnico.md`: cronologia ampliada y plan de continuidad.

Para una futura actualizacion, cambiar juntos los indicadores del encabezado, el progreso de entregas, la fecha del pie y los afiches correspondientes.
