import numpy as np

print("Class of numbers:")

print("Plus:")
print("2 + 2 = ", 2 + 2)
print("---------------")
print("Minus:")
print("2 - 2 = ", 2 - 2)
print("---------------")
print("Multiply:")
print("2 * 2 = ", 2 * 2)
print("---------------")
print("Division:")
print("2 / 2 = ", 2 / 2)
print("---------------")
print("Potency:")
print("2 ** 2 = ", 2 ** 2)
print("---------------")
print("Module:")
print("2 % 2 = ", 2 % 2)
print("---------------")
print("Expression:")
print("((2 + 2) * (5 - 7) * 2) / 5 = ", ((2 + 2) * (5 - 7) * 2) / 5)
print("")
print("(2 + 2) * (2 - 2) / 0 = ")
try:
    (2 + 2) * (2 - 2) / 0
except:
    print("Oops, não pode fazer divisão com zero!")
print("")
print("")
print("---------------")
print("Variables:")
i = 90
name = "Jhon Doe"
print("i = ", i)
print("name = ", name)
print("")
print("")
print("---------------")
print("Matriz:")
a = [[0, 1, 2, 3, 4, 5],
     [0, 1, 2, 3, 4, 5],
     [0, 1, 2, 3, 4, 5],
     [0, 1, 2, 3, 4, 5],
     [0, 1, 2, 3, 4, 5]]

print(np.matrix(a))
print("")
print("")
print("---------------")
print("Operators:")
print("(1 > 2) and (2 < 3) = ", (1 > 2) and (2 < 3))
print("(1 > 2) or (2 < 3) = ", (1 > 2) or (2 < 3))
print("(1 == 1) and (2 == 2) = ", (1 == 1) and (2 == 2))
