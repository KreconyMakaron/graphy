from sympy.plotting import plot
from sympy import simplify 

def get_range(s):
    arr = s.split(',')
    if len(arr) == 1:
        return None, None
    if len(arr) == 2:
        return (float(arr[0]), float(arr[1])), None
    if len(arr) == 4:
        return (float(arr[0]), float(arr[1])), (float(arr[2]), float(arr[3]))
    raise ValueError('numebr of commas is wrong!! either use 1 for xlim or 3 for xlim and ylim')

def plt(s):
    expr = s.split('|')
    xlim, ylim = (get_range(expr[-1])) if len(expr) > 1 else (None, None)

    if xlim is not None:
        expr = expr[:-1]

    expr = [simplify(x) for x in expr]
    return plot(*expr, xlim=xlim, ylim=ylim, show=False), ", ".join(str(a) for a in expr), xlim, ylim
