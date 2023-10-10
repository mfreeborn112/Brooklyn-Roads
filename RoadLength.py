import geopandas as gpd
import pandas as pd

def calculate_lengths(data):
    """
    Calculate total lengths for all roads and for roads with protected bike lanes.
    
    Parameters:
    - data: Filtered GeoDataFrame
    
    Returns:
    - Tuple with two values: Total length for all roads, total length for roads with bike lanes, both in miles.
    """
    # Conversion factor: feet to miles
    FEET_TO_MILES = 5280.0
    
    # Total length for all roads
    total_length_all = data['shape_leng'].sum() / FEET_TO_MILES
    
    # Filter for roads with bike lanes
    bike_lanes = data[data['bike_lane'] == '1']
    
    # Total length for roads with bike lanes
    total_length_bike_lanes = bike_lanes['shape_leng'].sum() / FEET_TO_MILES

    return total_length_all, total_length_bike_lanes

if __name__ == "__main__":
    
    # Load the cleaned Brooklyn data
    brooklyn_data = gpd.read_file('Clean Brooklyn Street Centerlines.geojson')
    
    # Calculate lengths
    total_all, total_bike_lanes = calculate_lengths(brooklyn_data)
    
    # Create a DataFrame for the results and save to CSV
    results = pd.DataFrame({
        'Road Type': ['All Roads', 'Protected Bike Lanes'],
        'Road Length (miles)': [total_all, total_bike_lanes]
    })
    
    results.to_csv("Clean Brooklyn Streets.csv", index=False)
