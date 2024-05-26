def solve_linear_equation():
    equation = input("Введіть рівняння (наприклад, 'x + 5 = 12'): ")

    left_side, right_side = equation.split('=')
    left_side = left_side.strip()
    right_side = right_side.strip()

    if 'x' in left_side:
        expression, result = left_side, right_side
        unknown_on_left = True
    else:
        expression, result = right_side, left_side
        unknown_on_left = False

    result = float(result)

    if '+' in expression:
        parts = expression.split('+')
        if 'x' in parts[0]:
            a = float(parts[1].strip())
            x = result - a
        else:
            a = float(parts[0].strip())
            x = result - a

    elif '-' in expression:
        parts = expression.split('-')
        if 'x' in parts[0]:
            a = float(parts[1].strip())
            x = result + a
        else:
            a = float(parts[0].strip())
            x = a - result

    elif '*' in expression:
        parts = expression.split('*')
        if 'x' in parts[0]:
            a = float(parts[1].strip())
            x = result / a
        else:
            a = float(parts[0].strip())
            x = result / a

    elif '/' in expression:
        parts = expression.split('/')
        if 'x' in parts[0]:
            a = float(parts[1].strip())
            x = result * a
        else:
            a = float(parts[0].strip())
            x = a / result

    else:
        return "Невідома операція."

    if unknown_on_left:
        print(f"x = {x}")
    else:
        print(f"{x} = x")


