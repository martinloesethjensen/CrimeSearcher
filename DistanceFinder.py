from geopy.distance import great_circle

def __get_lon_lat():
    from urllib.request import urlopen
    import json
    with urlopen("http://ipinfo.io/json") as url:
        json_data = json.loads(url.read().decode())
        return str(json_data["loc"])


def calculate_distance(other_loc):
    print(great_circle(__get_lon_lat(), str(other_loc)).km)
