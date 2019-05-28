import simple_colors

from service import csv_parser, printer, value_checker


def get_input(desc) -> int:
    user_input = input(desc)
    try:
        value = int(user_input)
        return value
    except ValueError:
        return 0


def get_crimes_from_term(search_term: str, category: str) -> list:
    print(simple_colors.yellow(f'Search term: {search_term}\n'
                               f'Category: {category}'))
    return [row for row in get_crime_list() if row[category] == search_term.upper()]


def get_category():
    return value_checker.check_search_value(get_input(simple_colors.yellow("Please enter a number: ")))


def search():
    search_quit = "0"
    category = ""

    while search_quit == "0":
        printer.print_categories()
        search_quit = category = get_category()

    if category != "-1":
        search_term = input("Search: ")
        results = get_crimes_from_term(search_term, category)
        printer.print_results(results)


# get crime list from csv file
def get_crime_list() -> list:
    return csv_parser.load_csv_to_list("csv-files/SacramentocrimeJanuary2006.csv")


if __name__ == '__main__':
    is_quit = False
    while not is_quit:
        printer.print_main_menu()
        is_quit = value_checker.check_value(get_input(simple_colors.yellow("Please enter a number: ")))
    exit()
