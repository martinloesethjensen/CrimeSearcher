import csv


# Read the contents from csv file and return a dict
def load_csv_to_list(csv_file: str) -> list:  # TODO: modularize method and find new name
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        crime_list = []

        for row in csv_reader:
            crime_list.append(row)

        return crime_list
