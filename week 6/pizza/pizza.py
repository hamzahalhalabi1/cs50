import tabulate
import csv
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]
    if not file_name.endswith('.csv'):
        sys.exit("Not a CSV file")
    else:
        table = table_maker()
        print(table)


def table_maker():
    try:
        menu = []
        with open(sys.argv[1]) as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                menu.append(row)
        return tabulate.tabulate(menu[1:], menu[0], tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
