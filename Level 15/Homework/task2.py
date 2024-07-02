def main():
    # რაოდენობის შეყვანა
    while True:
        try:
            quantity = int(input("გთხოვთ, შეიყვანოთ ნივთების რაოდენობა, რომლის შეძენაც გსურთ: "))
            if quantity > 0:
                break
            else:
                print("რაოდენობა უნდა იყოს დადებითი რიცხვი.")
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი მთელი რიცხვი.")

    total_cost = 0
    items_entered = 0

    # ფასების შეყვანა
    while items_entered < quantity:
        try:
            price = float(input(f"შეიყვანეთ ფასი ნივთისთვის #{items_entered + 1}: "))
            if price > 0:
                total_cost += price
                items_entered += 1
            else:
                print("ფასი უნდა იყოს დადებითი რიცხვი.")
        except ValueError:
            print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")

    # შედეგის გამოტანა
    print(f"ნივთების მთლიანი ღირებულება: {total_cost} ლარი")

if __name__ == "__main__":
    main()