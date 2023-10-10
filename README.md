# Brooklyn Road Analysis

## Goal:
This project aims to load, clean, and analyze a dataset with geospatial data about roads in Brooklyn. Our primary goal is to quantify the amount of total road length and compare it with the length dedicated to bike lanes. Post analysis, these results can be visualized effectively using a Tableau dashboard.

## Repository Contents:

### Data:

1. `NYC Street Centerline (CSCL).zip`
    - Description: Original dataset sourced from NYC Open Data.
2. `Clean Brooklyn Street Centerlines.geojson`
    - Description: The cleaned geojson file that has been processed and filtered for ease of visualization in Tableau.
3. `Clean Brooklyn Streets.csv`
    - Description: A succinct CSV file containing data about the total length of roads in Brooklyn and the length dedicated to bike lanes.

### Scripts:

1. `PrepGeoJsonFile.py`
    - Description: This Python script takes the original dataset as input and processes it to produce a clean geospatial file. This cleaned file can then be further analyzed in Tableau or any other geospatial analysis tool.
2. `RoadLength.py`
    - Description: A Python script that reads the cleaned geospatial file, calculates the total road length and the length dedicated to bike lanes, and then outputs the results in a CSV format.

## Getting Started:

1. **Preparation**: Ensure you have the required libraries installed. Typically, `geopandas` and `pandas` would be necessary for such scripts.
2. **Data Preparation**: Run `PrepGeoJsonFile.py` to process the raw data and obtain a clean GeoJSON file suitable for geospatial analysis.
3. **Analysis**: Execute `RoadLength.py` to obtain a CSV containing the total lengths of roads and bike lanes in Brooklyn.
4. **Visualization**: Load the cleaned GeoJSON file or the output CSV into Tableau to visualize and derive insights from the data.
