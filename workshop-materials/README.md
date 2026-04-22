# `workshop-materials/`

Material fuente del **Workshop 1 — Fundamentos de Spec-Driven Development con GitHub Copilot** (EY, 22 de abril de 2026).

Este directorio contiene todos los artefactos que los participantes copiarán o usarán durante los hands-on. Está organizado por tipo de artefacto, no por slide.

## Estructura

```
workshop-materials/
├── custom-instructions/
│   ├── profiles/                      # Hands-on 3 (slide 17)
│   │   ├── senior-dev.md
│   │   ├── consultor.md
│   │   └── aprendiz.md
│   └── base/
│       └── copilot-instructions.md    # Hands-on 5 (slide 31)
├── prompts/
│   ├── business-analyst/              # Hands-on 6 (slide 34)
│   │   ├── seed-prompt.md
│   │   └── feature-description.md
│   └── structured-review/             # Hands-on 8 (slide 43)
│       └── seed-prompt.md
├── agents/
│   └── code-reviewer/                 # Hands-on 7 (slide 39)
│       ├── seed-prompt.md
│       └── code-reviewer.agent.md     # Plan B pre-hecho
├── skills/
│   └── pdf-summarizer/                # Hands-on 9 (slide 46)
│       ├── SKILL.md
│       └── scripts/
│           └── extract_text.py
├── samples/
│   ├── sample.pdf                     # PDF de prueba para hands-on 9
│   └── sample.txt                     # Fuente del PDF
├── sample-code/
│   └── user_service.py                # Archivo Python para revisar (hands-on 7 y 8)
└── mcp/
    └── context7.json                  # Hands-on 10 (slide 49)
```

## Mapeo a hands-on

| Hands-on | Slide | Origen (este repo) | Destino en el repo del participante |
|---|---|---|---|
| 3 · Efecto de las instrucciones | 17 | `custom-instructions/profiles/*.md` | `.github/copilot-instructions.md` (uno a la vez) |
| 5 · Crear `copilot-instructions.md` base | 31 | `custom-instructions/base/copilot-instructions.md` | `.github/copilot-instructions.md` |
| 6 · Prompt file `business-analyst` | 34 | `prompts/business-analyst/seed-prompt.md` + `feature-description.md` | `.github/prompts/business-analyst.prompt.md` |
| 7 · Custom agent `code-reviewer` | 39 | `agents/code-reviewer/seed-prompt.md` (o `code-reviewer.agent.md` como Plan B) | `.github/agents/code-reviewer.agent.md` |
| 8 · `code-reviewer` + `structured-review` | 43 | `prompts/structured-review/seed-prompt.md` | `.github/prompts/structured-review.prompt.md` |
| 9 · Skill `pdf-summarizer` | 46 | `skills/pdf-summarizer/` (carpeta completa) + `samples/sample.pdf` | `.github/skills/pdf-summarizer/` |
| 10 · MCP `context7` | 49 | `mcp/context7.json` | `.vscode/mcp.json` |

Para los hands-on 7 y 8, el archivo a revisar es `sample-code/user_service.py` (contiene problemas intencionales de seguridad, manejo de errores y nombres para que el revisor tenga material).

## Convenciones

- Idioma: español (textos y prompts). Los identificadores de código quedan en inglés.
- Frontmatter YAML alineado con la documentación oficial de GitHub Copilot:
  - Custom instructions → `code.visualstudio.com/docs/copilot/customization/custom-instructions`
  - Prompt files → `code.visualstudio.com/docs/copilot/customization/prompt-files`
  - Custom agents → `code.visualstudio.com/docs/copilot/customization/custom-agents`
  - Agent skills → `code.visualstudio.com/docs/copilot/customization/agent-skills`
  - MCP → `code.visualstudio.com/docs/copilot/customization/mcp-servers`
- Custom agent en formato **GA de VS Code** (`*.agent.md`, no `*.chatmode.md`).
- Custom agent `code-reviewer` con `tools` **read-only** (sin `edit`/`run`) — por construcción no puede modificar archivos.
- Skill `pdf-summarizer` con `description` específica (menciona _trigger_) para que el matching automático funcione.
- MCP `context7` apunta al endpoint HTTP oficial (`https://mcp.context7.com/mcp`).

## Regenerar el PDF de muestra

```bash
cupsfilter workshop-materials/samples/sample.txt > workshop-materials/samples/sample.pdf
```

(En Linux: usar `enscript … | ps2pdf -` o `pandoc sample.txt -o sample.pdf`.)
