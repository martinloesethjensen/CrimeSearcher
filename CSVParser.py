import csv


# Read the contents from csv file and return a dict
def load_csv(csv_file: str):
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        # for logging
        line_count = 0
        for row in csv_reader:

            # Columns
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            print(f'Crime: {row["crimedescr"]}')
        # end of logging

        return csv_reader


if __name__ == '__main__':
    load_csv("csv-files/SacramentocrimeJanuary2006.txt")
