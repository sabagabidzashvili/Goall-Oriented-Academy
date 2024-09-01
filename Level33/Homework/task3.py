def calculator(num1, num2):
    action = int(input("select 1 for +, select 2 for -, select 3 for *, select 4 for /"))
    if action == 1:
        print(num1 + num2)
    elif  action == 2:
        print(num1 - num2)
    elif action == 3:
        print(num1 * num2)
    elif action == 4:
        if num2 == 0:
            print("შეცდომა: ნულზე გაყოფა შეუძლებელია")
        else:
            print(num1 / num2)

calculator(2, 0)
