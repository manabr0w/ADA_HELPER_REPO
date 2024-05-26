import math

def solve_quadratic():
    print("Введіть коефіцієнти квадратного рівняння ax^2 + bx + c = 0")

    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        roots = (root1, root2)

    elif discriminant == 0:
        root = -b / (2*a)
        roots = (root,)

    else:
        roots = None

    if roots:
        print("Корені рівняння:", roots)
    else:
        print("Рівняння не має дійсних коренів")

