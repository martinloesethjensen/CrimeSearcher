import csv


# Read the contents from csv file and return a dict
def load_csv(csv_file: str) -> list:
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        crime_dict = []
        line_count = 0

        for row in csv_reader:
            crime_dict.append(row)
            # Columns
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            print(f'Crime: {row["crimedescr"]}')

        return crime_dict


if __name__ == '__main__':
    load_csv("csv-files/SacramentocrimeJanuary2006.txt")
