import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search("https*://(www\.)*youtube.com/embed/([a-z_A-Z0-9]+)", s):
        return "https://youtu.be/" + link.group(2)

if __name__ == "__main__":
    main()


#stupid way
# import re
#
#
# def main():
#     print(parse(input("HTML: ")))
#
#
# def parse(s):
#     if "youtube.com/embed/xvFZjo5PgG0" in s:
#         return "https://youtu.be/xvFZjo5PgG0"
#     else:
#         return None
#
#
# if __name__ == "__main__":
#     main()

