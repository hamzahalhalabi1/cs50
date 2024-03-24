# # my answer
# menu = {
#     "Baja Taco": 4.00,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }
# menu = {key.lower(): value for key, value in menu.items()}
# total = 0
#
# while True:
#     # Take user input
#     user_input = input("Item: ").lower()
#
#     try:
#         price = menu[user_input]
#         total += price
#         print(f"Total:{total}0")
#     except KeyError:
#         pass


#answer for the cs50
menu= {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input('Item: ').title()
        if item in menu:
            total += menu[item]
            print("Total: $", end= "")
            print("{:.2f}".format(total))
    except EOFError:
        print()
        break