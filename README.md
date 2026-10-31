# Travel ADK Multiagent - Laboratorio UCV

Sistema Multiagente de Viajes desarrollado con Google ADK, Python, Poetry, Pytest y GitHub Actions.

## Agentes Especializados
- **Travel Coordinator Agent**: Agente principal que coordina a los subagentes.
- **Web Search Agent**: Realiza búsquedas de información actualizada con Google Search.
- **Itinerary Agent**: Planifica itinerarios detallados día a día.
- **Budget Agent**: Estima presupuestos de viaje.
- **Risk Reviewer Agent**: Evalúa riesgos comunes (clima, altura, seguridad).
- **Local Culture Agent** *(Reto)*: Recomienda platos típicos, costumbres y frases útiles.

## Instalación y Ejecución
```bash
python -m venv .venv
source .venv/Scripts/activate
pip install poetry
poetry install