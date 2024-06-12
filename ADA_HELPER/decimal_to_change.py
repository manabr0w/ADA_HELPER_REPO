def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")


def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")


def decimal_to_change():
    decimal = int(input("Введіть число у десятковій системі числення: "))

    conversion_functions = {
        "бінарна": decimal_to_binary,
        "шістнадцяткова": decimal_to_hexadecimal,
        "вісімкова": decimal_to_octal
    }

    while True:
        print("Оберіть систему числення:")
        print("1. Бінарна")
        print("2. Шістнадцяткова")
        print("3. Вісімкова")
        choice = input("Ваш вибір (Бінарна/Шістнадцяткова/Вісімкова): ").lower()

        conversion_function = conversion_functions.get(choice)
        if conversion_function:
            result = conversion_function(decimal)
            print(f"Представлення числа {decimal} у вибраній системі: {result}")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


# Run the function
decimal_to_change()
