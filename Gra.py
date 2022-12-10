from random import randint

number = randint(0, 101)

while True:

    try:

        choice = int(input("Guess the number:"))

        if choice == number:
            print("You win!")
            break

        if choice < number:
            print("Too small!")

        if choice > number:
            print("Too big!")

    except ValueError:
        print("It's not a number")
