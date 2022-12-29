import cmath
def solve_quadric_equation(a, b, c):
    try:
        d = (b ** 2) - (4 * a * c)
        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        return f'The solution are x1={complex(x1)} and x2={complex(x2)}'
    except ZeroDivisionError:
        return 'Zero Division Error'
    except:
        return 'Could not convert string to float'