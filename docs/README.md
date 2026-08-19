# SafePath Documentation & Design Blueprints

This directory contains the baseline architectural specifications, data strategies, mathematical risk models, database schemas, and API contracts for **SafePath**.

## Specification Documents Hierarchy

1. **[Requirements Specification](./requirements/README.md)** — Product Requirements Specification (PRS) Version 1.1.
2. **[Technical & Database Architecture](./architecture/README.md)** — Technical Architecture Version 1.0 & Database Architecture Version 1.2.
3. **[Data Architecture & Strategy](./data/README.md)** — Data Architecture & Data Source Strategy Version 1.0.
4. **[Safety Intelligence & Risk Model](./risk-model/README.md)** — Safety Intelligence & Risk Model Specification Version 1.1.
5. **[API Contract Architecture](./api/README.md)** — API Specification & Endpoint Definitions Version 1.2.

---

## Architectural Principles
* **Privacy by Design:** Ephemeral active journey location buffers; zero permanent user movement traces.
* **Modular Monolith:** Strict software module boundaries within a unified, high-performance FastAPI codebase.
* **Explainable Risk Intelligence:** Decoupled risk scores and confidence levels with transparent human-readable explanations.
