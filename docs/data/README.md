# Data Architecture & Strategy — Version 1.0

## Baseline Summary

The SafePath Data Architecture transforms open safety data, OpenStreetMap road networks, public transit feeds (GTFS), and crowdsourced reports into normalized spatial-temporal risk maps.

### Data Ingestion Strategy:
1. **OpenStreetMap (OSM):** Road geometry, footways, sidewalk tags, and street lighting attributes.
2. **Historical Crime Feeds:** Open government datasets (e.g. NYC Open Data, UK Police API, Telangana/Hyderabad open statistics).
3. **GTFS Transit Static Feeds:** Bus and Metro station stops for late-night activity accessibility scoring.
4. **Sunrise-Sunset / Weather APIs:** Real-time daylight and weather context.

### Spatial Aggregation (Uber H3):
* Uber H3 hexagonal grid indexing (Resolution 9, ~0.1 km² cell area) used for efficient spatial aggregation and risk lookups.

### Data Provenance:
* Every derived feature and risk score is linked to immutable provenance records (`data_provenance_records` and `risk_estimate_evidence`).
