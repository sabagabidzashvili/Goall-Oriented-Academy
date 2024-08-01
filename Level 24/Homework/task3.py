def check_scores():
    try:
        midterm_score = float(input("შეიყვანეთ შუალედური გამოცდის ქულა (0-დან 100-მდე): "))
        final_score = float(input("შეიყვანეთ დასკვნითი გამოცდის ქულა (0-დან 100-მდე): "))
        project_score = float(input("შეიყვანეთ პროექტის ქულა (0-დან 100-მდე): "))

        if not (0 <= midterm_score <= 100 and 0 <= final_score <= 100 and 0 <= project_score <= 100):
            print("ყველა ქულა უნდა იყოს 0-დან 100-მდე.")
            return

        average_score = (midterm_score * 0.2) + (final_score * 0.4) + (project_score * 0.4)

        if average_score >= 70:
            print(f"სტუდენტმა ჩააბარა კურსი. საშუალო ქულა: {average_score:.2f}")
        else:
            print(f"სტუდენტმა ვერ ჩააბარა კურსი. საშუალო ქულა: {average_score:.2f}")

    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვები.")

check_scores()