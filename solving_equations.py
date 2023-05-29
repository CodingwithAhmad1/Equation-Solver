from sympy import *

a,b,c,x,y,z = symbols('a,b,c,x,y,z', real=True)

# you can edit this to write any equation
expr = (5*((x-9)**2)) + (3*(x-9))
print(expr.factor()) # factorises any equation


expression = Eq((x+5)/2, 7/x)
solution = solveset(expression) # solves a set of equation

print(solution)






