##MY WAY
# import sys
# import csv
#
#
# def main():
#     file_path = sys.argv[1]
#     output_file = sys.argv[2]
#     validate_file(file_path)
#     output = changer(file_path)
#     release(output, output_file)
#
# def release(output, output_file):
#     header_texts = ["first", "last", "address"]
#     with open(output_file, "a") as file:
#         for line in output:
#             file.write(line + '\n')
#
#
# def changer(file_path):
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         biglist = []
#         for line in reader:
#             print(line)
#             opposite_name, address = line
#             first_and_second_name_list = opposite_name.rsplit(",")
#             second_name = first_and_second_name_list[0]
#             first_name = first_and_second_name_list[-1].lstrip()
#             ordered_name = f"{first_name}, {second_name}"
#             biglist.append(ordered_name + ',' + address)
#         return biglist
#
#
# def validate_file(file_path):
#     if len(sys.argv) < 3:
#         sys.exit("Too few command-line arguments")
#     elif len(sys.argv) > 3:
#         sys.exit("Too many command-line arguments")
#     if not file_path.endswith('.csv'):
#         sys.exit("Not a CSV file")
#     try:
#         with open(file_path):
#             pass
#     except FileNotFoundError:
#         sys.exit("Could not read invalid_file.csv")
#
#
# if __name__ == "__main__":
#     main()

##Chatgpt
# import csv
# import sys
#
#
# def clean_and_write_csv(input_file, output_file):
#     try:
#         with open(input_file, 'r') as csvfile:
#             reader = csv.DictReader(csvfile)
#             fieldnames = ['first', 'last', 'house']
#
#             with open(output_file, 'w', newline='') as outfile:
#                 writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#                 writer.writeheader()
#
#                 for row in reader:
#                     full_name = row['name'].strip('""')
#                     last_name, first_name = map(str.strip, full_name.split(','))
#                     writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})
#
#
#
#     except FileNotFoundError:
#         sys.exit(f"Could not read {input_file}")
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         sys.exit("Too few or too many command-line arguments. Please provide input and output file names.")
#
#     input_file, output_file = sys.argv[1], sys.argv[2]
#     clean_and_write_csv(input_file, output_file)

#Smart guy
import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, "w") as output:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames = header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()