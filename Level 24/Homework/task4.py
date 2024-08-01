def check_license_eligibility():
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    experience = int(input("რამდენი წელია, რაც მანქანას მართავთ: "))

    if age >= 18 and experience >= 1:
        print("თქვენ გაქვთ მართვის მოწმობის აღების უფლება.")
    elif age < 18:
        print("თქვენ არ გაქვთ ასაკის უფლება მართვის მოწმობის მისაღებად.")
    else:
        print("თქვენ არ გაქვთ საკმარისი გამოცდილება მართვის მოწმობის მისაღებად.")

check_license_eligibility()