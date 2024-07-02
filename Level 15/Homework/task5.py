def main():
    while True:
        try:
            age = float(input("შეიყვანეთ თქვენი ასაკი: "))
            if age <= 0:
                print("ასაკი უნდა იყოს დადებითი რიცხვი. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    
    while True:
        try:
            total_purchase = float(input("შეიყვანეთ შესყიდვის მთლიანი თანხა ($): "))
            if total_purchase <= 0:
                print("შესყიდვის თანხა უნდა იყოს დადებითი რიცხვი. გთხოვთ, სცადოთ კვლავ.")
                continue
            break
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    
    if age > 60 and total_purchase >= 100:
        discount = 20
    elif age > 60:
        discount = 15
    elif total_purchase >= 100:
        discount = 10
    else:
        discount = 0

    if discount > 0:
        print(f"თქვენ გაქვთ {discount}% ფასდაკლება.")
    else:
        print("თქვენ არ გაქვთ ფასდაკლების უფლება.")

if __name__ == "__main__":
    main()
