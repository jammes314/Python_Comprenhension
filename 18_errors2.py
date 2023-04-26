try:

    print(0/0)
    assert 1 != 1 , ' uno no es igual a uno '
    age = 10 
    if age <18:
    raise Exception("Age must be more than 18")

    
except ZeroDivisionError as error:
    print(error)    
except AssertionError as error:
    print(error)
except Exception as error:
    print()
print("hola")
