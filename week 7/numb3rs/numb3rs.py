import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        a, b, c, d = map(int, ip.split('.'))
        if 0 <= a < 256 and 0 <= b < 256 and 0 <= c < 256 and 0 <= d < 256:
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    main()