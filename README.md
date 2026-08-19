# SafePath — Preventive Safety Intelligence & Journey Companion Platform

SafePath is a serious software platform designed for preventive travel safety intelligence and active journey companionship. Rather than relying solely on travel distance or duration, SafePath evaluates contextual safety metrics—such as historical incident data, street lighting coverage, public activity signals, verified community reports, and temporal risk variations—to recommend safer routes and support travelers in real time.

---

## System Architecture Baseline

This repository is structured as a **Modular Monolith** supporting clear domain boundaries, privacy-by-design principles, and zero-trace location ephemerality for active journeys.

### Approved Specification Documents
All baseline engineering specifications are maintained in the [`docs/`](./docs/) directory:
* **Product Requirements Specification:** [PRS Version 1.1](./docs/requirements/README.md)
* **Technical Architecture:** [Technical Architecture Version 1.0](./docs/architecture/README.md)
* **Data Architecture & Strategy:** [Data Architecture Version 1.0](./docs/data/README.md)
* **Safety Intelligence & Risk Model:** [Risk Model Version 1.1](./docs/risk-model/README.md)
* **Database Architecture:** [Database Architecture Version 1.2](./docs/architecture/README.md)
* **API Contract Specification:** [API Specification Version 1.2](./docs/api/README.md)

---

## Directory Structure

```
SafePath/
├── backend/          # Python 3.11+ FastAPI modular monolith backend
├── frontend/         # React 18 + TypeScript + Vite + MapLibre GL JS frontend
├── data/             # Spatial-temporal data pipeline storage (raw, processed, sample)
├── scripts/          # Ingestion, pre-processing, and deployment helper scripts
├── docs/             # Formally versioned specifications and design blueprints
├── tests/            # Cross-cutting integration and system end-to-end tests
├── docker-compose.yml# Local container orchestration definition
└── .gitignore        # Version control exclusion rules
```

---

## Technology Stack

* **Frontend:** React 18, TypeScript, Vite, MapLibre GL JS.
* **Backend:** Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, Celery.
* **Database:** PostgreSQL 16 + PostGIS 3.4, Uber H3 spatial grid indexing.
* **Cache / Ephemeral Store:** Redis 7 (volatile active location buffers, session cache, task queue broker).
* **Routing Engine Placeholder:** OpenStreetMap-compatible routing engine (Valhalla / OSRM integration point).

---

## Getting Started (Local Development Scaffold)

### Prerequisites
* Python 3.11+
* Node.js v20+ / npm v10+
* Docker & Docker Compose

### 1. Running Backend Locally
```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```
The FastAPI application will start at `http://localhost:8000`. Test the health endpoint at `http://localhost:8000/health/liveness`.

### 2. Running Frontend Locally
```bash
cd frontend
npm install
npm run dev
```
The Vite development server will start at `http://localhost:5173`.

### 3. Running via Docker Compose
```bash
docker-compose up --build
```

---

## License & Governance
SafePath is strictly governed by privacy-by-design standards:
1. High-frequency active location updates remain strictly ephemeral within Redis buffers and are hard-deleted post-journey.
2. Safety scores represent contextual estimates and do not guarantee physical safety.
