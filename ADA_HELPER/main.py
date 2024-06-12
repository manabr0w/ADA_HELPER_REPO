from quadratic_equations import solve_quadratic
from linear_equations import solve_linear_equation
from get_capitals import get_capital
from decimal_to_change import decimal_to_change
from matrix_math import matrix_operation
from show_weather import get_weather_info

def main():
    list_of_operations = [
        "1. Вирішити лінійне рівняння",
        "2. Вирішити квадратне рівняння",
        "3. Знайти столицю країни",
        "4. Перевести число з десяткової в іншу систему",
        "5. Операції з матрицями",
        "6. Переглянути погоду в місті",
        "7. Завершити програму"
    ]

    operations_dict = {
        "1": solve_linear_equation,
        "2": solve_quadratic,
        "Вирішити квадратне рівняння": solve_quadratic,
        "3": get_capital,
        "Знайти столицю країни": get_capital,
        "4": decimal_to_change,
        "Перевести число з десяткової в іншу систему": decimal_to_change,
        "5": matrix_operation,
        "Операції з матрицями": matrix_operation,
        "6": get_weather_info,
        "Переглянути погоду в місті": get_weather_info,
        "7": lambda: print("Програма завершена.") or exit(),
        "завершити програму": lambda: print("Програма завершена.") or exit(),
        "end": lambda: print("Програма завершена.") or exit()
    }

    while True:
        print("Щоб вибрати операцію, введіть номер операції або назву українською мовою:")
        for operation in list_of_operations:
            print(operation)

        question = input('Ваш вибір: ')
        operation = operations_dict.get(question.lower())
        if operation:
            operation()
        else:
            print("Неправильний вибір операції.")

if __name__ == '__main__':
    main()
