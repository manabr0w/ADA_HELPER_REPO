def decimal_to_change():
    decimal = int(input("Введіть число у десятковій системі числення: "))

    while True:
        print("Оберіть систему числення:")
        print("1. Бінарна")
        print("2. Шістнадцяткова")
        print("3. Вісімкова")
        choice = input("Ваш вибір (Бінарна/Шістнадцяткова/Вісімкова): ").lower()

        if choice in ["бінарна", "1"]:
            result = bin(decimal).replace("0b", "")
            print(f"Двійкове представлення числа {decimal}: {result}")
            break
        elif choice == "шістнадцяткова":
            result = hex(decimal).replace("0x", "")
            print(f"Шістнадцяткове представлення числа {decimal}: {result}")
            break
        elif choice == "вісімкова":
            result = oct(decimal).replace("0o", "")
            print(f"Вісімкове представлення числа {decimal}: {result}")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


