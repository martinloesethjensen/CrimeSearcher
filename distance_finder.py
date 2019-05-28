from geopy.distance import great_circle


def __get_lon_lat():
    from urllib.request import urlopen
    import json
    with urlopen("http://ipinfo.io/json") as url:
        json_data = json.loads(url.read().decode())
        temp_var = (json_data["loc"]).split(",")
        temp_var = [float(data) for data in temp_var]
        return tuple(temp_var)


def calculate_distance(other_loc):
    distance = great_circle(__get_lon_lat(), other_loc)
    return distance


def get_scanned_locations_list(data_list):
    scanned_list = []
    for item in data_list:
        coords = (item["latitude"], item["longitude"])
        if calculate_distance(coords) < 5.0:
            scanned_list.append(item)
    return scanned_list
