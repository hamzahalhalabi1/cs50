try:
    inputs = []
    while True:
        user_input = input("Name: ")
        inputs.append(user_input)
except EOFError:
    # Ctrl+D is pressed, handling the end of input
    if len(inputs) == 1:
        result = inputs[0]
    elif len(inputs) == 2:
        result = " and ".join(inputs)
    else:
        result = ", ".join(inputs[:-1]) + ", and " + inputs[-1]

    existing_text = "Adieu, adieu, to "
    final_text = existing_text + result
    print(final_text)
