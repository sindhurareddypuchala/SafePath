# Safety Intelligence & Risk Model Specification — Version 1.1

## Baseline Summary

The SafePath Risk Model estimates contextual travel risk from multi-source spatial-temporal evidence while maintaining explicit separation between **Risk Score ($R \in [0, 100]$)** and **Confidence Score ($C \in [0, 100]$)**.

### Model Features & Pipeline:
1. **Bounded Evidence Quality Weighting:** $q_i \in [0, 1]$ based on source reliability priors, freshness, spatial/temporal accuracy, and saturating corroboration factors.
2. **Responsible Absence-of-Evidence Rule:** Missing data or missing OSM tags reduce Confidence ($C$), but never serve as direct proof of high risk.
3. **Feature-Specific Temporal Modulation:** Temporal multipliers applied per-feature (e.g. lighting is strongly nighttime-dependent; static geometry is constant).
4. **Confidence-Weighted Shrinkage:** Blends local segment risk estimates with regional priors based on segment data confidence.
5. **Multi-Metric Route Confidence:** Captures length-weighted average confidence, percent low-confidence distance, and worst-segment confidence.
6. **Separated Alert Engine Logic:** Route deviation tracking and environmental safety risks are evaluated independently.
