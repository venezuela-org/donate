# Datos abiertos — 600 kits para crear

Paquete público de referencia para el reto **Del kit al impacto**. Corte: **10 de octubre de 2026**. No es un registro individual de niños ni un inventario en tiempo real.

## Archivos

| Archivo | Contenido | Estado |
| --- | --- | --- |
| `resumen_2026-10-10.csv` | Totales comprobados y su fecha de corte | Datos públicos existentes |
| `presupuesto_2026-10-10.csv` | Porcentajes del balance ya publicado | Datos públicos existentes |
| `composicion_kit.csv` | Componentes previstos por kit | Datos públicos existentes |
| `entregas_publicas_plantilla.csv` | Columnas admitidas para futuras entregas verificadas | Plantilla vacía; **no contiene entregas** |

Fuente primaria: el [estado publicado](https://github.com/venezuela-org/donate/blob/main/README.md) y la [cronología](https://github.com/venezuela-org/donate/blob/main/docs/cronologia-y-plan-tecnico.md) del proyecto. Si el estado cambia, añadir un nuevo corte fechado en lugar de sobrescribir el anterior.

## Uso responsable

- `kits_armados = kits_entregados + kits_pendientes` para este corte: 600 = 509 + 91.
- Los 60 dibujos **recibidos** no son 60 dibujos autorizados para publicación.
- La plantilla de entregas requiere verificación por el equipo local antes de incorporar filas. Usar localidad general, sin coordenadas exactas de entrega ni escuelas asociadas con participantes.
- El registro privado de entregas y consentimientos se mantiene **fuera del repositorio**, como explica [la especificación de privacidad](https://github.com/venezuela-org/donate/blob/main/docs/gallery-data-spec.md).
- Para demostraciones con eventos individuales, generar datos sintéticos claramente marcados y no sumarlos a los totales reales.

## Licencias

Los datos estructurados de este paquete se ofrecen bajo [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Este README y el diccionario original se ofrecen bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), con atribución a Creative Commons Venezuela.

**Los dibujos y fotografías quedan fuera de esta dedicación.** La autorización para exhibir un dibujo no implica por sí sola permiso para aplicarle CC BY ni otra licencia abierta; cada archivo requiere consentimiento y alcance documentados.
