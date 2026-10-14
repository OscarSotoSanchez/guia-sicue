"""Genera los códigos QR (SVG) que usa index.html.

Si cambia algún enlace, actualízalo aquí y en el HTML, y vuelve a ejecutar generar-pdf.sh.
Requiere: pip install --user segno
"""
import pathlib

import segno

QR = {
    "web": "https://www.urjc.es/programa-de-movilidad-de-estudiantes-sicue",
    "convenios": "https://www.urjc.es/images/Intranet/sicue/2026_2027/Convenios%20SICUE%2026_27.pdf",
    "impreso-c": "https://www.urjc.es/images/Intranet/sicue/2026_2027/Impreso_C_Acuerdo_Academico%20salientes%20URJC%2026-27.pdf",
    "manual": "https://www.urjc.es/images/Intranet/sicue/2026_2027/MANUAL_DEL_ESTUDIANTE_SICUE%20_%20SALIENTE%202026-27.pdf",
    "plazos": "https://www.urjc.es/images/Intranet/sicue/2026_2027/Plazos%20SICUE%20SALIENTES%20%202026-27.pdf",
    "sede": "https://sede.urjc.es",
    "guias": "https://gestion3.urjc.es/guiasdocentes/",
    "plantilla": "https://oscarsotosanchez.github.io/guia-sicue/propuesta-acuerdo-academico-SICUE.xlsx",
    "guia": "https://oscarsotosanchez.github.io/guia-sicue/",
}

out = pathlib.Path(__file__).resolve().parent / "qr"
out.mkdir(exist_ok=True)
for name, url in QR.items():
    segno.make(url, error="m").save(out / f"{name}.svg", scale=4, border=1, dark="#1F3A5F")
    print(f"qr/{name}.svg -> {url}")
