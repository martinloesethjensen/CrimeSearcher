import CSVParser


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


def check_value(value):
    if value == 0:
        print("Not a valid option...")
        return False
    elif value == -1:
        print("Quiting...")
        return True

    # TODO: add last option when functionality is done.

    return False


if __name__ == '__main__':
    # get crime list from csv file
    crime_list = CSVParser.load_csv("csv-files/SacramentocrimeJanuary2006.txt")

    is_quit = False
    while not is_quit:
        main_menu()
        is_quit = check_value(get_input())
    exit()
