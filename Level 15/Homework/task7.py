def main():
    gpa = float(input("შეიყვანეთ თქვენი GPA: "))
    family_income = float(input("შეიყვანეთ თქვენი ოჯახის შემოსავალი ($): "))

    is_eligible = gpa >= 3.0 and family_income < 50000

    eligibility_message = "თქვენ გაქვთ სტიპენდიის უფლება." if is_eligible else "თქვენ არ გაქვთ სტიპენდიის მიღების უფლება."

    print(eligibility_message)

main()
