import csv


# Read the contents from csv file and return a dict
def load_csv_to_list(csv_file: str) -> list:
    try:
        with open(csv_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            return [crime for crime in csv_reader]
    except FileNotFoundError:
        print("File not found.")


# Write new reported record to csv file
def write_record_to_csv(csv_file: str, crimes: list):
    try:
        with open(csv_file, mode='w') as csv_file:
            column = "cdatetime,address,district,beat,grid,crimedescr,ucr_ncic_code,latitude,longitude\n"
            csv_file.write(column)

            for crime in crimes:
                row = "{cdatetime},{address},{district},{beat},{grid},{crimedescr},{ucr_ncic_code},{latitude},{longitude}\n" \
                    .format(cdatetime=crime['cdatetime'],
                            address=crime['address'],
                            district=crime['district'],
                            beat=crime['beat'],
                            grid=crime['grid'],
                            crimedescr=crime['crimedescr'],
                            ucr_ncic_code=crime['ucr_ncic_code'],
                            latitude=crime['latitude'],
                            longitude=crime['longitude'])
                csv_file.write(row)
    except Exception:
        print("Something unknown happened")
