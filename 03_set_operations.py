set_a = {'col', 'mex', 'bol'} 
set_b = {'pe', 'bol'}

set_c= set_b.union(set_a)

print(set_c)

print(set_b | set_a)

set_d = set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)

## Diferencia ##
set_1 = set_a.difference(set_b)
print(set_1)
print(set_a - set_b)
## symmetric difference ##
set_2 = set_a.symmetric_difference(set_b)
print(set_2)
print(set_a ^ set_b)

