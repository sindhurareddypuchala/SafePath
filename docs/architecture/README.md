# Technical & Database Architecture Specifications

## Technical Architecture Version 1.0 & Database Architecture Version 1.2

### High-Level Architecture
SafePath is implemented as a **Modular Monolith** in Python FastAPI with PostgreSQL/PostGIS and Redis.

### System Components:
1. **Frontend:** React 18 + TypeScript + Vite + MapLibre GL JS SPA.
2. **API Gateway & Layer:** FastAPI Async Controller with JWT & HttpOnly cookie auth.
3. **Application Services:** 10 domain modules (Auth, Users, Navigation, Safety Intelligence, Community, Journey, Companion, Alerts, Vehicles, Image Analysis, Analytics).
4. **Data Access Layer:** SQLAlchemy 2.0 async ORM with PostGIS spatial query extensions.
5. **Caching & Ephemeral Store:** Redis 7 (In-memory GPS stream buffers, session states, task queue broker).
6. **Background Task Processing:** Celery async task workers.
7. **Routing Engine Integration:** Valhalla / OSRM routing engine integration via dynamic cost multipliers.

### Database Schema Highlights (Version 1.2):
* 28 normalized tables supporting spatial grid indexing (`h3_spatial_cells`), community reporting lifecycle, multi-metric route confidence, and evidence provenance mapping (`risk_estimate_evidence`).
