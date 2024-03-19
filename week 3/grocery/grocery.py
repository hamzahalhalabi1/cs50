list = {}

while True:
    try:
        key = input("").lower()
        if key in list:
            list[key] +=1
        else:
            list[key] = 1

    except EOFError:
        for a in sorted(list.keys()):
            print(list[a], a.upper())
        break