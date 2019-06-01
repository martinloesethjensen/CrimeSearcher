import json
from urllib.request import urlopen

from geopy.distance import great_circle


# Getting lon and lat from ip location
def __get_lon_lat():
    with urlopen("http://ipinfo.io/json") as url:
        json_data = json.loads(url.read().decode())
        temp_var = (json_data["loc"]).split(",")
        temp_var = [float(data) for data in temp_var]
        return tuple(temp_var)


def calculate_distance_current(other_loc):
    try:
        distance = great_circle(__get_lon_lat(), other_loc)
        return distance
    except:
        print("Error! Could not retrieve location or data input was faulty.")


def calculate_distance(src_loc, other_loc):
    try:
        distance = great_circle(src_loc, other_loc)
        return distance
    except:
        print("Incorrect values were passed, please try again.")

