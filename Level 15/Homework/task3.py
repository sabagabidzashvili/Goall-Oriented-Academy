def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_health_message(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    while True:
        try:
            weight = float(input("გთხოვთ, შეიყვანოთ თქვენი წონა (კილოგრამებში): "))
            if weight <= 0:
                print("წონა უნდა იყოს დადებითი რიცხვი. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")

    while True:
        try:
            height = float(input("გთხოვთ, შეიყვანოთ თქვენი სიმაღლე (მეტრებში): "))
            if height <= 0:
                print("სიმაღლე უნდა იყოს დადებითი რიცხვი. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")

    bmi = calculate_bmi(weight, height)
    health_message = get_health_message(bmi)

    print(f"თქვენი BMI არის: {bmi:.2f}")
    print(f"ჯანმრთელობის სტატუსი: {health_message}")

if __name__ == "__main__":
    main()