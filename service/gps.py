import datetime

import simple_colors
from geopy.distance import great_circle

from service import printer
from service.parser import csv_parser


def __get_lon_lat():
    from urllib.request import urlopen
    import json
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


def get_scanned_locations_list(data_list, src_loc=None):

    scanned_list = []

    try:
        for item in data_list:
            coords = (item["latitude"], item["longitude"])

            if src_loc is None:
                if calculate_distance_current(coords) < 5.0:
                    scanned_list.append(item)
            else:
                if calculate_distance(src_loc, coords) < 5.0:
                    scanned_list.append(item)

        if len(scanned_list) is 0:
            print("No crimes in proximity!")
        return scanned_list

    except:
        print("Error in data! Tried to parse", coords)


def print_crimes_by_proximity(crime_list, src_loc=None):
    use_current_loc = (
        input(simple_colors.magenta("If you want to input your own longitude and latitude, please input 1.\n"
                                    "If you wish to use your current location, input 2! WARNING: THIS COULD TAKE A LOT OF TIME DEPENDING ON LOCATION!")))

    if use_current_loc is "1":
        src_loc = (input(simple_colors.red("Longitude & Latitude: ")))
        scanned_list = get_scanned_locations_list(crime_list, src_loc)
        printer.print_results(scanned_list)

        __write_crimes_by_proximity_csv(scanned_list)

    elif use_current_loc is "2":
        scanned_list = get_scanned_locations_list(crime_list, src_loc)
        print(simple_colors.magenta("Started searching with CURRENT location..."))
        printer.print_results(scanned_list)

        __write_crimes_by_proximity_csv(scanned_list)


def __write_crimes_by_proximity_csv(scanned_list):
    csv_write_request = (
        input(simple_colors.magenta("Do you want your new data in a CSV file?\n"
                                    "Input 1 for YES,\n"
                                    "Input 2 for NO")))
    if csv_write_request is "1":

        curr_datetime = datetime.datetime.now()
        curr_datetime.strftime('%m-%d-%y %H-%M')
        curr_datetime = curr_datetime.replace(microsecond=0)
        curr_datetime = str(curr_datetime)
        curr_datetime = curr_datetime.replace(":", "-")
        csv_parser.write_record_to_csv(str(curr_datetime), scanned_list)

        print(simple_colors.magenta("Data has been written to CSV: " + curr_datetime))
    elif csv_write_request is "2":
        print(simple_colors.magenta("No CSV will be printed..."))
