with open('text.txt', 'w+',  ) as file:
    for line in file:
        print(line)
    file.write('neue worten\n')
    file.write('holiii boli\n')
