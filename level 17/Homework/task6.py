target_number = 77

while True:
    try:
        guess = int(input("Enter a number: "))
        if guess == target_number:
            print("Congratulations! You guessed the number.")
            break
        else:
            print("Wrong number, try again.")
    except ValueError:
        print("Please enter a valid number.")






















