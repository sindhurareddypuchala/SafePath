# SafePath Data Directory

This directory stores spatial-temporal datasets used by the ingestion and risk feature generation pipelines.

## Subdirectories
* `raw/`: Unprocessed open crime CSVs, OpenStreetMap PBF files, and municipal shapefiles. (Ignored in Git).
* `processed/`: Processed spatial vector layers and compiled H3 grid risk cache tables. (Ignored in Git).
* `sample/`: Synthetic/anonymized sample datasets for unit testing and local offline development.
