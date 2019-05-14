import csv


# Read the contents from csv file and return a dict
def load_csv(csv_file: str) -> list:
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        crime_dict = []

        for row in csv_reader:
            crime_dict.append(row)

        return crime_dict
