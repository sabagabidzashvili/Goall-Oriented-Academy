def main():
    while True:
        try:
            gpa = float(input("შეიყვანეთ თქვენი GPA: "))
            if gpa < 0 or gpa > 4:
                print("GPA უნდა იყოს 0-დან 4-მდე. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    
    while True:
        try:
            family_income = float(input("შეიყვანეთ თქვენი ოჯახის შემოსავალი ($): "))
            if family_income < 0:
                print("შემოსავალი უნდა იყოს დადებითი რიცხვი. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    
    if gpa >= 3.5:
        scholarship = "სრული სტიპენდია"
    elif gpa >= 3.0 and family_income < 50000:
        scholarship = "უმაღლესი სტიპენდია"
    elif gpa >= 3.0:
        scholarship = "სტიპენდია"
    else:
        scholarship = "სტიპენდიის უფლება არ გაქვთ"

    print(f"თქვენი GPA: {gpa}")
    print(f"ოჯახის შემოსავალი: ${family_income}")
    print(f"სტიპენდიის სტატუსი: {scholarship}")

if __name__ == "__main__":
    main()
