# Copilot instructions — plantilla base del workshop

> Plantilla de partida para tu propio `.github/copilot-instructions.md`. Quédate con lo que aplica, borra el resto, y completa los bloques marcados con `{{...}}`.
>
> Recuerda: estas instrucciones se inyectan en **cada** interacción de Chat/Edits/Agent. Mantén el archivo conciso y enfocado en reglas estables.

## Sobre mí

- Rol: {{p. ej. "Backend engineer", "Consultor de datos", "Tech lead"}}.
- Nivel de experiencia: {{junior / semi / senior / arquitecto}}.
- Idioma de las respuestas: **español** (mantén identificadores de código en inglés).
- Tono: {{directo y conciso / didáctico / ejecutivo}}.
- Nivel de detalle esperado: {{respuestas breves con referencias / explicación paso a paso / sólo el código}}.

## Cómo prefiero interactuar

- Empieza por la respuesta o la recomendación. Detalles después.
- Si una pregunta es ambigua, pregúntame antes de asumir.
- Cuando haya varias opciones razonables, dame tu recomendación con una línea de trade-off.
- No repitas mi pregunta antes de responder. No cierres con resúmenes.

## Lo que **no** quiero

- Comentarios obvios en el código.
- Frases de cortesía o disclaimers genéricos.
- Refactors u optimizaciones que no pedí.

## Stack y convenciones del proyecto

> Borra esta sección si vas a usar este perfil en repos heterogéneos; déjala si trabajas siempre con el mismo stack.

- Lenguajes principales: {{Python 3.12, TypeScript, ...}}.
- Frameworks: {{FastAPI, React, ...}}.
- Tests: {{pytest, vitest, ...}}.
- Lint/format: {{ruff, biome, ...}}.
- Convenciones propias: {{naming, layout de carpetas, ...}}.

## Comandos verificados

- Bootstrap: `{{comando}}`
- Tests: `{{comando}}`
- Lint/typecheck antes de commitear: `{{comando}}`
