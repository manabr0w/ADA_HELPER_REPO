from quadratic_equations import solve_quadratic
from linear_equations import solve_linear_equation
from get_capitals import get_capital
from decimal_to_change import decimal_to_change
from matrix_math import matrix_operation
from show_weather import get_weather_info

def main():
    list_of_operations = ["1. Вирішити лінійне рівняння",
                          "2. Вирішити квадратне рівняння",
                          "3. Знайти столицю країни",
                          "4. Перевести число з десяткової в іншу систему",
                          "5. Операції з матрицями",
                          "6. Переглянути погоду в місті",
                          "7. Завершити програму"]

    while True:
        print("Щоб вибрати операцію, введіть номер операції або назву українською мовою:")
        for operation in list_of_operations:
            print(operation)

        question = input('Ваш вибір: ')
        if question == "1":
            solve_linear_equation()
        elif question == "2" or question == "Вирішити квадратне рівняння":
            solve_quadratic()
        elif question == "3" or question == "Знайти столицю країни":
            get_capital()
        elif question == "4" or question == "Перевести число з десяткової в іншу систему":
            decimal_to_change()
        elif question == "5" or question == "Операції з матрицями":
            matrix_operation()
        elif question == "6" or question == "Переглянути погоду в місті":
            get_weather_info()
        elif question == "7" or question.lower() == "end" or question.lower() == "завершити програму":
            print("Програма завершена.")
            break
        else:
            print("Неправильний вибір операції.")

if __name__ == '__main__':
    main()
