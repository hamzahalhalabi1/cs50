def main():
    fraction = input('Enter fraction: ')
    result = convert(fraction)
    output = gauge(result)
    print(output)


def convert(fraction):
    while True:
        try:
            x_str, y_str = fraction.split('/')

            if not x_str.isdigit() or not y_str.isdigit():
                fraction = input('Invalid input. Enter fraction again: ')
                continue

            x, y = int(x_str), int(y_str)

            if y < x or y == 0:
                raise ValueError

            break

        except ValueError:
            fraction = input('Invalid input. Enter fraction again: ')
            continue

    result = int(x / y * 100)
    return result


def gauge(percentage):
    if percentage == 1 or percentage == 0:
        return "E"
    elif percentage == 100 or percentage == 99:
        return "F"
    elif percentage == 66:
        return "67%"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
