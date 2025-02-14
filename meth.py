import sympy
from sympy.integrals.risch import NonElementaryIntegral

def diff(s):
    return sympy.pretty(sympy.diff(sympy.simplify(s)), use_unicode=False)

def intg(s):
    i = sympy.integrate(sympy.simplify(s))
    if type(i) is NonElementaryIntegral:
        return "idk"
    return sympy.pretty(i, use_unicode=False)

def simp(s):
    return sympy.pretty(sympy.simplify(s))
