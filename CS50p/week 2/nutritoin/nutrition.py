item = input('Item: ')


match item.lower():
    case "apple" | 'apples':
        calories = 130
    case 'avocado'| 'avocados':
        calories = 50
    case "kiwifruit"| "kiwifruits":
        calories = 90
    case 'pear'| 'pears':
        calories = 100
    case "grapefruit"| "grapefruits":
        calories = 60
    case 'sweet cherries'| 'sweet cherry':
        calories = 100
    case _:
        calories = 0

if calories == 0:
    print("")
else:
    print(f"Calories: {calories}")
