# Seed prompt · Generar el prompt file `structured-review`

> Pega este prompt en una **sesión nueva** de Copilot Chat. Devuelve el contenido completo de un prompt file que guardarás como `.github/prompts/structured-review.prompt.md`. Está diseñado para ejecutarse sobre el custom agent `code-reviewer` (Hands-on 7).

---

Genera el contenido **completo** de un archivo `.prompt.md` para GitHub Copilot llamado `structured-review.prompt.md`. La salida debe ir en un único bloque de código Markdown, sin texto antes ni después.

## Comportamiento esperado

El prompt file ejecuta una **revisión estructurada** sobre un archivo de código. El usuario lo invoca como `/structured-review` y entrega la ruta del archivo (o el archivo ya seleccionado). Acepta:

- Argumento `${input:targetFile:Ruta del archivo a revisar}` para la ruta.
- Si no se entrega ruta, usa `${selection}` como objetivo.

El revisor analiza **sólo el archivo indicado** (no expande a todo el repo), y devuelve la salida con **formato fijo**, en español.

## Formato de salida obligatorio

Cuatro secciones, en este orden, siempre presentes (vacías si no aplica):

```
## Resumen
Una a dos frases sobre el propósito del archivo y el estado general.

## Hallazgos por severidad

### 🔴 Bloqueantes
- [archivo:línea] Descripción del problema. Impacto. Cómo arreglarlo.

### 🟠 Importantes
- ...

### 🟡 Sugerencias
- ...

## Cobertura de revisión
Checklist marcado de qué dimensiones se evaluaron:
- [x] Corrección lógica
- [x] Seguridad
- [x] Manejo de errores
- [x] Tests
- [x] Legibilidad / nombres
- [x] Performance evidente

## Veredicto
APROBADO / APROBADO CON CAMBIOS / RECHAZADO — una frase de justificación.
```

## Reglas

- Mencionar siempre `archivo:línea` para cada hallazgo.
- No inventar problemas para llenar secciones — si no hay bloqueantes, dejar la sección con "Ninguno".
- No reescribir el archivo. No editar nada. Es una revisión, no una intervención.
- Si el archivo no existe o no se puede leer, decirlo y detenerse.

## Frontmatter

YAML con:
- `description`: una frase explicando que ejecuta una revisión estructurada con salida fija.
- `name`: `structured-review`.
- `argument-hint`: `targetFile`.
- `agent`: `code-reviewer` (asume que existe el custom agent del Hands-on 7).
- `tools`: limitar a tools de lectura (`['search/codebase', 'search/usages']`) — la revisión no debe tocar archivos.

## Formato de la respuesta

Devuelve **únicamente** el archivo dentro de un bloque ```` ```markdown ```` … ```` ``` ````.
