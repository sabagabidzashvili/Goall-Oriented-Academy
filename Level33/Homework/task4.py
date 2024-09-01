def calculator(num1, num2):
    action = int(input("select 1 for +, select 2 for /"))
    if action == 1:
        print(num1 + num2)
    elif action == 2:
        if num2 == 0:
            print("შეცდომა: ნულზე გაყოფა შეუძლებელია")
        else:
            print(num1 / num2)


calculator(2, 0)
