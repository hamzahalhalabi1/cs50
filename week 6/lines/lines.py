import sys


def main():
    number_of_lines = count_lines()
    print(number_of_lines)


def count_lines():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]
    if not file_name.endswith('.py'):
        sys.exit("Not a Python file")
    try:
        with open(file_name, 'r') as file:
            lines = 0
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:  # Skip empty lines
                    continue
                if stripped_line.startswith("#"):
                    lines -= 1
                if stripped_line.startswith(" "):
                    lines -= 1
                lines += 1

            return lines
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
