def solve_addition(parts, result):
    if 'x' in parts[0]:
        a = float(parts[1].strip())
        return result - a
    else:
        a = float(parts[0].strip())
        return result - a

def solve_subtraction(parts, result):
    if 'x' in parts[0]:
        a = float(parts[1].strip())
        return result + a
    else:
        a = float(parts[0].strip())
        return a - result

def solve_multiplication(parts, result):
    if 'x' in parts[0]:
        a = float(parts[1].strip())
        return result / a
    else:
        a = float(parts[0].strip())
        return result / a

def solve_division(parts, result):
    if 'x' in parts[0]:
        a = float(parts[1].strip())
        return result * a
    else:
        a = float(parts[0].strip())
        return a / result

def solve_linear_equation():
    equation = input("Введіть рівняння (наприклад, 'x + 5 = 12'): ")

    left_side, right_side = equation.split('=')
    left_side = left_side.strip()
    right_side = right_side.strip()

    x_in_left_side = 'x' in left_side

    if x_in_left_side:
        expression, result = left_side, right_side
    else:
        expression, result = right_side, left_side

    result = float(result)

    operations = {
        '+': solve_addition,
        '-': solve_subtraction,
        '*': solve_multiplication,
        '/': solve_division
    }

    for operator, function in operations.items():
        if operator in expression:
            parts = expression.split(operator)
            x = function(parts, result)
            break
    else:
        return "Невідома операція."

    if x_in_left_side:
        print(f"x = {x}")
    else:
        print(f"{x} = x")

