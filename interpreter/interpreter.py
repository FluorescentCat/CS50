x1, x2, x3 = input("Please give expression: ").split(" ")
x1 = float(x1)
x3 = float(x3)

#print(x1,x2,x3)

if x2 == "+":
    result = x1 + x3
elif x2 == "-":
    result = x1 - x3
elif x2 == "*":
    result = x1 * x3
elif x2 == "/" and x3 != 0:
    result = x1 / x3
else:
    result = "No valid calculation"

print(result)