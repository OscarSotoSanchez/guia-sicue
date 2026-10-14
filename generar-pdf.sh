#!/usr/bin/env bash
# Genera guia-sicue-alumno.pdf a partir de index.html (QR + Chrome headless).
# Uso: ./generar-pdf.sh
set -euo pipefail
cd "$(dirname "$0")"

python3 generar-qr.py

CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser)
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header \
  --print-to-pdf="$PWD/guia-sicue-alumno.pdf" "file://$PWD/index.html" 2>/dev/null

echo "PDF generado: $PWD/guia-sicue-alumno.pdf"
