
import tabulate
import csv
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py <file_path>")

    file_path = sys.argv[1]
    validate_file(file_path)

    table = table_maker(file_path)
    print(table)


def validate_file(file_path):
    if not file_path.endswith('.csv'):
        sys.exit("Not a CSV file")
    try:
        with open(file_path):
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")


def table_maker(file_path):
    menu = []
    try:
        with open(file_path) as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                menu.append(row)
        return tabulate.tabulate(menu, tablefmt="grid")
    except FileNotFoundError:
        return "File does not exist"

if __name__ == "__main__":
    main()
