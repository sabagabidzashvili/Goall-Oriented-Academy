def ask_for_password(correct_password):
    while True:
        password = input("Enter your password: ")
        if password == correct_password:
            print("Password correct!")
            break
        else:
            print("Incorrect password, try again.")
ask_for_password("mySecretPassword")
