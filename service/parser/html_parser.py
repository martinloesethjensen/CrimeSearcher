import os
import webbrowser


def beautify_data_html(data):
    beautiful_string = ""
    counter = 1
    for item in data:
        beautiful_string += """
        <tr>
            <td>id: {id}</td>
            <td>{cdatetime}</td> 
            <td>{address}</td> 
            <td>{district}</td> 
            <td>{beat}</td> 
            <td>{grid}</td> 
            <td>{crimedescr}</td> 
            <td>{ucr}</td> 
            <td>{lat}</td> 
            <td>{lon}</td> 
        </tr>
        """.format(id=counter,
                   cdatetime=item["cdatetime"],
                   address=item["address"],
                   district=item["district"],
                   beat=item["beat"],
                   grid=item["grid"],
                   crimedescr=item["crimedescr"],
                   ucr=item["ucr_ncic_code"],
                   lat=item["latitude"],
                   lon=item["longitude"])
        counter += 1

    return beautiful_string


def parse_html(data):
    html_file = open("output-files/dataset.html", "w")

    html_file.write("""
    <html>
        <head></head>
        <body>
            <table>
                <tr>
                    <th></th>
                    <th>cdatetime</th>
                    <th>address</th>
                    <th>district</th>
                    <th>beat</th>
                    <th>grid</th>
                    <th>crimedescr</th>
                    <th>ucr_ncic_code</th>
                    <th>latitude</th>
                    <th>longitude</th>
                </tr>
                    """ + beautify_data_html(data) + """
            </table>
        </body>
    </html>
    """)

    html_file.close()

    webbrowser.open("file://" + os.path.realpath("output-files/dataset.html"))
