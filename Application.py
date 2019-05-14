import CSVParser

global_crime_list = []


def get_input() -> int:
    user_input = input("Please enter a number: ")
    try:
        value = int(user_input)
        return value
    except ValueError:
        return 0


def main_menu():
    print()
    print("Enter 1: Search for a crime")
    print("Enter 2: Report a crime")
    print("Enter 3: Find crimes in proximity")
    print("Enter -1: Quit")
    print()


def get_crimes_from_term(search_term) -> list:
    return [row for row in global_crime_list if row['crimedescr'] == search_term.upper()]


def print_results(results):
    for result in results:
        print(result)


def search():
    search_term = input("Search: ")
    results = get_crimes_from_term(search_term)
    print_results(results)


def check_value(value):
    if value == 0:
        print("Not a valid option...")
        return False
    elif value == -1:
        print("Quiting...")
        return True
    elif value == 1:
        search()

    # TODO: add last option when functionality is done.

    return False


# get crime list from csv file
def get_crime_list() -> list:
    return CSVParser.load_csv_to_list("csv-files/SacramentocrimeJanuary2006.txt")


if __name__ == '__main__':
    crime_list = get_crime_list()

    global_crime_list = crime_list

    is_quit = False
    while not is_quit:
        main_menu()
        is_quit = check_value(get_input())
    exit()
