# Sistema de Agentes: Ghostwriter Ejecutivo para LinkedIn (CTO Edition)

Este repositorio contiene la arquitectura, prompts del sistema y flujo operativo de los agentes colaborativos diseñados para curar, validar, analizar y redactar contenido de liderazgo técnico para LinkedIn con voz de CTO experimentado.

---

## 🎯 Objetivo del Sistema

Transformar los eventos y novedades de ingeniería más relevantes de los últimos 7 días en **5 publicaciones estratégicas para LinkedIn**, eliminando el 100% del hype de marketing y enfocándose exclusivamente en tus áreas de expertise:
- IA aplicada al desarrollo de software y AI Assisted Development.
- Productividad de equipos de ingeniería, Developer Experience y SDLC.
- DevOps, CI/CD y Platform Engineering.
- Arquitecturas escalables y sistemas distribuidos.
- Liderazgo tecnológico, gestión ágil y cultura de ingeniería.

---

## 🤖 Los Agentes y sus Roles

| Agente | Nombre Interno | Rol Principal | Responsabilidad |
| :--- | :--- | :--- | :--- |
| **1. Scout Tecnológico** | `scout_curator` | Radar & Curador Especializado | Rastrea blogs de ingeniería de referencia y genera una **Shortlist de 8 a 10 temas** clasificados por pilares de tu perfil. |
| **🛑 Checkpoint Humano** | *Usuario (Tú)* | Validador Editorial | Seleccionas en 30 segundos los 5 temas que dominas y deseas publicar esa semana. |
| **2. Ghostwriter Ejecutivo** | `cto_ghostwriter` | Redactor estratégico | Genera el Resumen, Por qué importa, Tendencia, Opinión diferenciada y el Post de LinkedIn (250-500 palabras) para los 5 temas elegidos. |
| **3. Auditor de Calidad** | `editorial_auditor` | Gatekeeper y Editor en Jefe | Valida límites de palabras, ausencia de clichés ("game changer", "revolución"), consistencia de voz y ensambla el documento final. |
| **4. Director de Arte Visual** | `editorial_art_director` | Diseñador Visual Editorial | Traduce cada post auditado en un activo visual 1:1 de alto impacto (estética suiza minimalista) usando el skill `editorial-visuals`. |

---

## 🔄 Flujo Operativo con Validación Humana y Dirección de Arte

```mermaid
flowchart TD
    A["Fuentes de Ingeniería (Últimos 7 días)"] --> B["1. Scout Tecnológico\n(Shortlist de 8 a 10 candidatos con pilares)"]
    B --> C{{"🛑 CHECKPOINT DE VALIDACIÓN HUMANA\n(Tú seleccionas 5 temas en 30 segundos)"}}
    C -- "Temas confirmados: [1, 3, 5, 7, 8]" --> D["2. CTO Ghostwriter\n(5 Entregables + Post por tema)"]
    D --> E["3. Editorial Auditor\n(Auditoría de estilo, léxico y límites)"]
    E -- "Rechazo con feedback" --> D
    E -- "Aprobado (5 posts)" --> F["4. Director de Arte Visual\n(Skill: editorial-visuals -> image-generator)"]
    F --> G["Activos Visuales Ejecutivos 1:1\n(visuals/postX_ai.jpg)"]
    G --> H["Documento Semanal Consolidado\n(weekly_editorial_plan.md con texto e imágenes)"]
```

---

## 📁 Estructura del Proyecto

```text
.
├── README.md                      # Arquitectura y flujo operativo
├── .agents/
│   └── skills/
│       └── editorial-visuals/     # Skill para diseño de activos editoriales de LinkedIn
├── agents/
│   ├── scout.md                   # Configuración del Scout y filtros de especialidad
│   ├── ghostwriter.md             # Guía de estilo de CTO y estructura de entrega
│   ├── auditor.md                 # Checklist de tolerancia cero y reglas de auditoría
│   └── art_director.md            # Reglas de dirección de arte, arquetipos y motor visual
├── templates/
│   └── weekly_delivery_template.md # Plantilla oficial de entrega semanal
├── visuals/                       # Activos visuales 1:1 generados por el pipeline
└── weekly_editorial_plan.md       # Entrega consolidada de la semana (texto + imágenes)
```

---

## ✍️ Firma Intelectual

Todo el contenido generado se rige bajo la premisa:
> *«La IA no reemplaza el criterio. La tecnología por sí sola no genera resultados. Las ventajas competitivas provienen de la ejecución, la adopción y la capacidad organizacional.»*
