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
print("('io' == 'oi') = ", ('io' == 'oi'))
print("('oi' == 'oi') = ", ('oi' == 'oi'))
print("")
print("")
print("---------------")
print("if, elif, else:")
if 1 < 2:
    print('if 1 < 2 it will be print')
elif 2 < 1:
    print('it will not be print')
else:
    print('it will not be print too')
print("")
print("")
print("---------------")
print("For loop:")
seq = [1,2,3,4,5]
print('seq = ', seq)
print('for item in seq, do X thing')
for item in seq:
    print(item**2)
print("")
print('for item in range, print')
for item in range(0, 10):
    print(item)
print("")
print("")
print("---------------")
print("While loop:")
max = 10
i = 0
print('max = ', max)
print('while i < max, print i')
while i < max:
    print(i)
    i += 1
print("")
print("")
print("---------------")
print("List:")
out = []
print('Puts values into an empty list with 3 lines')
for item in range(5):
    out.append(item**2)
    print(out)
print("")
print('Puts values into an empty list with one line')
out2 = [item**2 for item in range(5)]
print(out2)
print("")
print("")
print("---------------")
print("Lambda:")
print("lambda var: var*2")
lambda var: var*2
print("")
print("")
print("---------------")
print("Map:")
seq = [1,2,3,4]
print("Map seq below")
print(seq)
print(list(map(lambda var: var*2, seq)))
print("")
print("")
print("---------------")
print("Filter:")
seq = [1,2,3,4]
print("Filter seq below")
print(seq)
print(list(filter(lambda item: item%2, seq)))
