# API Contract Architecture Specification — Version 1.2

## Baseline Summary

The SafePath API Surface connects the React frontend to the FastAPI modular backend over 12 domain endpoints.

### Key API Contracts:
1. **Navigation:** `POST /api/v1/routes/recommend` — Multi-criteria candidate route generation with attached risk summaries and explainability. Includes `data_snapshot_id` tracing.
2. **Journey Lifecycle:** `POST /api/v1/journey/start` — Explicit route binding, destination, transport mode, and consent timestamp.
3. **Telemetry Ingestion:** `POST /api/v1/journey/{id}/location` — High-frequency adaptive GPS telemetry update endpoint.
4. **Real-time SSE Stream:** `GET /api/v1/journey/{id}/stream` — Server-Sent Events stream for push alerts, deviation notifications, and check-in prompts.
5. **Companion Check-In:** `POST /api/v1/companion/check-in/ack` — Explicit check-in acknowledgment with status response (`SAFE`, `NEED_ASSISTANCE`, `MISSED_EXPIRED`).
6. **Trusted Contacts:** Full CRUD endpoints (`/api/v1/contacts`) plus journey-specific sharing authorization (`POST /api/v1/journey/{id}/share`).
7. **Community Reporting:** Submit, confirm, resolve, and flag hazard reports.
