from shapely.geometry import Point
from shapely.ops import transform
import pyproj

def find_intersecting_outlets(list_of_outlet, specific_outlet,distance_threshold=5000):
    intersecting_outlets = []
    if (len(list_of_outlet) and len(specific_outlet)) == 0:
        return []

    # Create a projection for measuring distances in meters
    proj_meters = pyproj.Transformer.from_crs(4326, 3857, always_xy=True).transform

    # Check for intersections with each outlet
    for outlet in list_of_outlet:
        outlet_point = Point(outlet['longitude'], outlet['latitude'])
        specific_outlet_point = Point(specific_outlet[0]['longitude'], specific_outlet[0]['latitude'])

        # Transform the points to meters for distance calculation
        outlet_point_meters = transform(proj_meters, outlet_point)
        specific_outlet_point_meters = transform(proj_meters, specific_outlet_point)

        # Calculate the distance between the outlets in meters
        distance = outlet_point_meters.distance(specific_outlet_point_meters)

        # If the distance is less than or equal to 5KM, add the outlet to the list
        if distance <= distance_threshold:
            intersecting_outlets.append({'latitude': outlet['latitude'], 'longitude': outlet['longitude']})

    return intersecting_outlets

# Example usage
# list_of_outlet = [{'latitude': 2.2708192, 'longitude': 102.2879377801564}, {'latitude': 2.14359, 'longitude': 102.426336}, {'latitude': 2.3609669, 'longitude': 102.0389737}, {'latitude': 2.2671313, 'longitude': 102.2440907}, {'latitude': 5.6018213, 'longitude': 100.5318806}, {'latitude': 2.1861929, 'longitude': 102.2565481210022}, {'latitude': 2.2841096, 'longitude': 102.1338866}, {'latitude': 2.1904762499999997, 'longitude': 102.25165620869464}, {'latitude': 2.44307365, 'longitude': 102.20463878772759}, {'latitude': 2.2795438, 'longitude': 102.3934007}, {'latitude': 2.3522253, 'longitude': 102.1089793}, {'latitude': -3.0118178, 'longitude': 104.7233137}, {'latitude': 2.255986, 'longitude': 102.2915442}, {'latitude': 2.22864075, 'longitude': 102.22720818620817}, {'latitude': 2.1975859, 'longitude': 102.2416113}]
# specific_outlet = [{'latitude': 2.2708192, 'longitude': 102.2879377801564}]

# intersecting_outlets = find_intersecting_outlets(list_of_outlet, specific_outlet)

# print(intersecting_outlets)
