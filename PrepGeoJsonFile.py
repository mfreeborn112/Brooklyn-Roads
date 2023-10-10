import geopandas as gpd

def filter_nyc_data(filepath):
    """
    Load and filter the NYC Street Centerline data for borocode=3.
    
    Parameters:
    - filepath: String path to the geojson file
    
    Returns:
    - GeoDataFrame with only the desired columns and filtered data.
    """
    
    # Load the geojson file into a GeoDataFrame
    gdf = gpd.read_file(filepath)

    # Filter for borocode = 3
    gdf_filtered = gdf[gdf['borocode'] == '3']

    # Keep only the desired fields
    gdf_filtered = gdf_filtered[['shape_leng', 'bike_lane', 'geometry', 'physicalid']]

    # Ensure shape_leng is a float
    gdf_filtered['shape_leng'] = gdf_filtered['shape_leng'].astype(float)

    return gdf_filtered

if __name__ == "__main__":
    # Load and filter data
    filtered_data = filter_nyc_data('NYC Street Centerline (CSCL).geojson')
    
    # Save the filtered data as a geojson file
    output_filepath = "Clean Brooklyn Streetlines.geojson"
    filtered_data.to_file(output_filepath, driver='GeoJSON')
