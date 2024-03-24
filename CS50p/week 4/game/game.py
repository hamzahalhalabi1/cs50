import random

while True:
    level_input = input("Level: ")

    try
        level = int(level_input)
        randomnumber = random.randint(1, level)

        while True:
            try:
                guess = int(input("Guess: "))
                if guess == randomnumber:
                    print("Just right!")
                    break
                elif guess > randomnumber:
                    print("Too large!")
                elif guess < randomnumber:
                    print("Too small!")
            except ValueError:
                pass
        break
    except ValueError:
        pass
