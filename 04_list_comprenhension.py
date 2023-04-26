

### [element for element in iterable ]

numbers = []

for element in range(1, 11):
    numbers.append(element *2 )
print(numbers)

numbers_2 = [ element* 2 for element in range(1,11)]
print(numbers_2)

for i in range(1, 101):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)


numbers_3 = [ element for element in range(1,101) if element % 2 != 0 ]
print(numbers_3)