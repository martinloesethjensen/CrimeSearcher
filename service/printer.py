import simple_colors


def print_categories():
    print(simple_colors.green("\n--- Categories ---"))
    print(simple_colors.magenta("Enter 1: Date and time \'1/1/06 0:00\'\n"
                                "Enter 2: Address \'3108 OCCIDENTAL DR\'\n"
                                "Enter 3: District \'2\'\n"
                                "Enter 4: Grid \'508\'\n"
                                "Enter 5: Crime description \'10851(A)VC TAKE VEH W/O OWNER\'\n"
                                "Enter 6: UCR NCIC CODE \'2404\'"))
    print(simple_colors.red("Enter -1: Go back\n"))


def print_export_options():
    print(simple_colors.green("\n--- Export Options ---"))
    print(simple_colors.magenta("Enter 1: JSON format\n"
                                "Enter 2: HTML format"))
    print(simple_colors.red("Enter -1: Don't export\n"))


def print_main_menu():
    print(simple_colors.green("\n--- Main Menu ---"))
    print(simple_colors.magenta("Enter 1: Search for a crime\n"
                                "Enter 2: Report a crime\n"
                                "Enter 3: Find crimes in proximity"))
    print(simple_colors.red("Enter -1: Quit\n"))


def print_results(results):
    print()
    counter = 0
    for result in results:
        counter += 1
        print(simple_colors.cyan(f'Result {counter}:\n\t{"cdatetime:" :20} {result["cdatetime"]}'
                                 f'\n\t{"address:" :20} {result["address"]}'
                                 f'\n\t{"district:" :20} {result["district"]}'
                                 f'\n\t{"beat:" :20} {result["beat"]}'
                                 f'\n\t{"grid:" :20} {result["grid"]}'
                                 f'\n\t{"crimedescr:" :20} {result["crimedescr"]}'
                                 f'\n\t{"ucr_ncic_code:" :20} {result["ucr_ncic_code"]}'
                                 f'\n\t{"latitude:" :20} {result["latitude"]}'
                                 f'\n\t{"longitude:" :20} {result["longitude"]}'))

    print(simple_colors.cyan(f'Results: {len(results)}'))


def print_record(result):
    print(simple_colors.cyan(f'\t{"cdatetime:" :20} {result["cdatetime"]}'
                             f'\n\t{"address:" :20} {result["address"]}'
                             f'\n\t{"district:" :20} {result["district"]}'
                             f'\n\t{"beat:" :20} {result["beat"]}'
                             f'\n\t{"grid:" :20} {result["grid"]}'
                             f'\n\t{"crimedescr:" :20} {result["crimedescr"]}'
                             f'\n\t{"ucr_ncic_code:" :20} {result["ucr_ncic_code"]}'
                             f'\n\t{"latitude:" :20} {result["latitude"]}'
                             f'\n\t{"longitude:" :20} {result["longitude"]}'))
