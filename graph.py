from sympy.plotting import plot
from sympy import simplify, symbols

def get_range(str):
    arr = str.split(',')
    if len(arr) == 1:
        return None
    if len(arr) > 2:
        raise ValueError('more than one comma in range :(')
    return (symbols('x'), float(arr[0]), float(arr[1]))

def plt(str):
    expr = str.split('|')
    r = get_range(expr[-1])
    if r is None:
        expr = [simplify(x) for x in expr]
        print(expr)
        return plot(*expr, show=False)
    else:
        expr = expr[:-1]
        print(expr, ' in range ', r)
        expr = [simplify(x) for x in expr]
        return plot(*expr, r, show=False)

