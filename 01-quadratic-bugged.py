# Debugging Active Learning Session - CSCI101
# Bugged File #2

import math

# Get input equation from user
# We want to make a list in the format of [variable, a, b, c]
# given an equation in the form a(variable)^2 + b(variable) + c (like 1x^2 - 2x + 1)
equation = input("Equation: ")
equation.replace(" ", "")

# Want to extract out variable and then coefficients
coef=[]
squared_index = equation.find("^2")
variable = equation[squared_index-1]
coef.append(variable)
a = int(equation[:equation.find(variable)]
coef.append(a)
b = int(equation[squared_index + 2:equation.find(variable, squared_index+1)])
coef.append(b)
c = int(equation[equation.find(variable, squared_index+1) + 1:])
coef.append(c)

#Now solve for the roots
a = coef[0]
b = coef[1]
c = coef[2]

#Use the quadratic equation to get both roots
roots=[]
roots.append((-b + math.sqrt(pow(b, 2) - (4*a*c)))/(2*a))
roots.append((-b + math.sqrt(pow(b, 2) - (4*a*c)))/(2*a))

print(coef[0], "=", roots[0])
print(coef[0], "=", roots[1])
