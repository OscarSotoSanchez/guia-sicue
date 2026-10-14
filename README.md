# Guía SICUE · ETSII · URJC

Guía rápida del programa de movilidad nacional **SICUE** para estudiantes de los grados de la ETSII (URJC) coordinados por Óscar Soto Sánchez: Diseño y Desarrollo de Videojuegos, Ingeniería de Computadores, Ingeniería del Software, Ingeniería Informática, Inteligencia Artificial y Matemáticas.

🌐 **Web:** <https://sicue-etsii.sotos.dev/>
📄 **PDF:** <https://sicue-etsii.sotos.dev/guia-sicue-alumno.pdf>
📊 **Plantilla Excel de propuesta de acuerdo académico:** <https://sicue-etsii.sotos.dev/propuesta-acuerdo-academico-SICUE.xlsx>

> Documento orientativo. La información oficial y vinculante es la publicada en <https://www.urjc.es/programa-de-movilidad-de-estudiantes-sicue>.

## Ficheros
| Fichero | Qué es |
|---|---|
| `index.html` | La guía (web). También es la fuente del PDF: en pantalla muestra la barra de descargas; al imprimir, 8 páginas A4. |
| `guia-sicue-alumno.pdf` | PDF generado a partir de `index.html`. |
| `propuesta-acuerdo-academico-SICUE.xlsx` | Plantilla que rellenan los alumnos salientes antes del Impreso C. |
| `generar-qr.py` | Genera los QR de `qr/` (requiere `pip install --user segno`). |
| `generar-pdf.sh` | Regenera los QR y el PDF con Google Chrome headless. |

## Actualizar cada curso
1. En `index.html`, buscar los comentarios `FECHAS` y `CONVENIOS` y actualizar fechas, destinos y el pie con la versión.
2. Cambiar las URLs `2026_2027` de los documentos oficiales en `index.html` y `generar-qr.py`.
3. `./generar-pdf.sh`
4. Commit y push: GitHub Pages publica en uno o dos minutos.
