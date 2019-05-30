import os
import webbrowser


def beautify_data_json(data):
    beautiful_string = ""

    last_item = len(data)

    counter = 1

    for item in data:
        beautiful_string += "{"
        beautiful_string += """
            \"cdatetime\": \"{cdatetime}\",
            \"address\": \"{address}\",
            \"district\": \"{district}\",
            \"beat\": \"{beat}\",
            \"grid\": \"{grid}\",
            \"crimedescr\": \"{crimedescr}\",
            \"ucr_ncic_code\": \"{ucr}\",
            \"latitude\": \"{lat}\",
            \"longitude\": \"{lon}\"
        """.format(cdatetime=item["cdatetime"],
                   address=item["address"],
                   district=item["district"],
                   beat=item["beat"],
                   grid=item["grid"],
                   crimedescr=item["crimedescr"],
                   ucr=item["ucr_ncic_code"],
                   lat=item["latitude"],
                   lon=item["longitude"])

        beautiful_string += "},\n\t\t" if not counter == last_item else "}\n"

        counter += 1

    return beautiful_string


def parse_json(data):
    with open("output-files/dataset.json", "w") as json_file:
        json_file.write("""[
        """ + beautify_data_json(data) + """]""")

    json_file.close()

    webbrowser.open("file://" + os.path.realpath("output-files/dataset.json"))
