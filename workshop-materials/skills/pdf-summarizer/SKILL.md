---
name: pdf-summarizer
description: Usa esta skill cuando el usuario pida resumir, sintetizar o extraer puntos clave de un archivo PDF del workspace. Activa el flujo de extracción de texto + resumen estructurado en bullets. No usar para PDFs remotos (URLs) ni para imágenes.
---

# PDF Summarizer

Procedimiento para resumir un PDF del workspace.

## 1. Localiza el PDF

- Si el usuario indicó una ruta, úsala.
- Si no, busca en el workspace archivos `*.pdf` recientes y pregunta cuál.
- Si no encuentras ninguno, dilo y detente.

## 2. Extrae el texto

Usa el script auxiliar `scripts/extract_text.py` con `python3`:

```bash
python3 .github/skills/pdf-summarizer/scripts/extract_text.py <ruta-al-pdf>
```

El script imprime el texto plano del PDF a stdout. Si falla por falta de dependencias, indica al usuario que instale `pypdf` (`pip install pypdf`) y detente — no intentes otros parsers ni inventes el contenido.

## 3. Resume

Devuelve el resumen con **este formato fijo**, en español:

```
## Resumen ejecutivo
Una a dos frases que capturan el propósito y la conclusión principal.

## Puntos clave
- Bullet 1
- Bullet 2
- ...
(entre 3 y 7 bullets, ordenados de más a menos importante)

## Datos relevantes
- Cifras, fechas, nombres propios o referencias citables.
(omitir esta sección si el documento no tiene datos cuantificables)

## Acciones / decisiones
- Lo que el lector debería **hacer** o **decidir** después de leerlo.
(omitir si el documento es puramente descriptivo)
```

## Reglas

- **No inventes** contenido que no esté en el PDF. Si el texto extraído es ilegible (PDF escaneado sin OCR), dilo y detente.
- Cita textualmente sólo cuando aporte (entre comillas y con la página si es posible).
- Si el PDF es muy largo (>20 páginas), avisa antes de resumir y pregunta si quieres un resumen por sección.
