

import functools


numbers = [1, 2 , 3, 4, 5, 6, 7, 8]

def accum(counter, item):

    print('counter: ' , counter )
    print('item: ' , item)
    return counter + item

result = functools.reduce(accum, numbers)

result  = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

