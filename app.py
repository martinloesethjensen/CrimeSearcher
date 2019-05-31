import simple_colors

from service import printer, value_checker
from service.parser import csv_parser, html_parser, json_parser


def get_number_input(desc) -> int:
    user_input = input(desc)
    try:
        value = int(user_input)
        return value
    except ValueError:
        return 0


def get_crimes_from_term(search_term: str, category: str) -> list:
    print(simple_colors.yellow(f'Search term: {search_term}\n'
                               f'Category: {category}'))
    return list(filter(lambda row: row[category] == search_term.upper(), get_crime_list()))


def get_category():
    return value_checker.check_search_value(get_number_input(simple_colors.yellow("Please enter a number: ")))


def get_export_format():
    return value_checker.check_export_value(get_number_input(simple_colors.yellow("Please enter a number: ")))


def search():
    search_quit, export_quit = 2 * "0"
    export_format, category = "", ""

    while search_quit == "0":
        printer.print_categories()
        search_quit = category = get_category()

    if category != "-1":
        search_term = input("Search: ")
        results = get_crimes_from_term(search_term, category)
        printer.print_results(results)
        while export_quit == "0" and len(results) != 0:
            printer.print_export_options()
            export_quit = export_format = get_export_format()
            if export_format == "json":
                json_parser.parse_json(results)
            elif export_format == "html":
                html_parser.parse_html(results)
            if export_format != "-1":
                print(simple_colors.yellow(
                    "--- Exported to {export_format} file ---".format(export_format=export_format.upper())))
                print(simple_colors.yellow("--- File is located in 'output-files' folder ---"))


def report_crime():
    crimes = get_crime_list()
    new_crime = {}
    print(simple_colors.yellow("--- Report new crime ---"))
    new_crime['cdatetime'] = input(simple_colors.yellow("\tcdatetime: "))
    new_crime['address'] = input(simple_colors.yellow("\taddress: "))
    new_crime['district'] = get_number_input(simple_colors.yellow("\tdistrict: "))
    new_crime['beat'] = input(simple_colors.yellow("\tbeat: "))
    new_crime['grid'] = get_number_input(simple_colors.yellow("\tgrid: "))
    new_crime['crimedescr'] = input(simple_colors.yellow("\tcrimedescr: "))
    new_crime['ucr_ncic_code'] = get_number_input(simple_colors.yellow("\tucr_ncic_code: "))
    new_crime['latitude'] = input(simple_colors.yellow("\tlatitude: "))
    new_crime['longitude'] = input(simple_colors.yellow("\tlongitude: "))
    print(simple_colors.yellow("\n--- Saved new crime ---"))
    printer.print_record(new_crime)
    crimes.append(new_crime)
    csv_parser.write_record_to_csv("csv-files/SacramentocrimeJanuary2006.csv", crimes)


# get crime list from csv file
def get_crime_list() -> list:
    return csv_parser.load_csv_to_list("csv-files/SacramentocrimeJanuary2006.csv")


if __name__ == '__main__':
    is_quit = False
    while not is_quit:
        printer.print_main_menu()
        is_quit = value_checker.check_value(get_number_input(simple_colors.yellow("Please enter a number: ")))
    exit()
