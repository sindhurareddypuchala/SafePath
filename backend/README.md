# SafePath Backend API & Service Engine

FastAPI modular monolith backend service for SafePath safety intelligence, route recommendations, active journey tracking, and companion check-ins.

## Directory Structure
* `app/core/`: Application settings, environment configuration, logging middleware.
* `app/api/`: Main API router and top-level endpoint definitions.
* `app/modules/`: Domain modules enforcing strict software boundaries:
  - `auth/`: Authentication & token management placeholders.
  - `users/`: User profiles and preferences placeholders.
  - `navigation/`: Route recommendations and explainability placeholders.
  - `safety_intelligence/`: Spatial risk calculation and H3 grid index placeholders.
  - `community/`: Crowdsourced incident reports placeholders.
  - `journey/`: Safe Journey mode state machine placeholders.
  - `companion/`: Periodic check-in prompt placeholders.
  - `alerts/`: Alert generation and notification placeholders.
  - `vehicles/`: Active journey vehicle metadata placeholders.
  - `image_analysis/`: On-demand surroundings vision processing placeholders.
  - `analytics/`: Anonymized spatial analytics placeholders.
* `app/database/`: SQLAlchemy database session setup and Redis connection management.
* `app/services/`: Cross-cutting application services.
* `app/main.py`: FastAPI entrypoint and health endpoints.

## Running Locally
```bash
python -m venv venv
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```
Health Endpoint: `http://localhost:8000/health/liveness`
