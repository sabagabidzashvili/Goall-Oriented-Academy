import random

def guess_number():
    # მომხმარებლის რიცხვის მოთხოვნა
    number_to_guess = int(input("გთხოვთ შეიყვანოთ რიცხვი 1-დან 100-მდე: "))

    while number_to_guess < 1 or number_to_guess > 100:
        number_to_guess = int(input("არასწორი მნიშვნელობა. გთხოვთ, შეიყვანოთ რიცხვი 1-დან 100-მდე: "))

    # პროგრამის მიერ რიცხვის გამოცნობის მცდელობა
    guess = random.randint(1, 100)
    tries = 1

    while guess != number_to_guess:
        print(f"გამოცნობა #{tries}: {guess}")
        guess = random.randint(1, 100)
        tries += 1

    print(f"მიღებული რიცხვი {guess}. პროგრამამ გამოიცნო {tries} მცდელობის შემდეგ!")

# პროგრამის გაშვება
guess_number()