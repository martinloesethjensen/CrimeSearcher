import json
from urllib.request import urlopen

from geopy.distance import great_circle


# Fetches the longitude and latitude of user from third party site and returns in tuple
def __get_lon_lat():
    with urlopen("http://ipinfo.io/json") as url:
        json_data = json.loads(url.read().decode())
        temp_var = (json_data["loc"]).split(",")
        temp_var = [float(data) for data in temp_var]
        return tuple(temp_var)


# Calculates distance between source lon/lat and target lon/lat using great_circle
# and returns the distance in KM
def calculate_distance(src_loc, other_loc):
    try:
        distance = great_circle(src_loc, other_loc)
        return distance
    except:
        print("Incorrect values were passed, please try again.")

