

# manzanas = [fertilizante , fijador , fungicida
# ]

# claudias = [ dormex]

# citricos = [ insecticida ]


def increment(x):
    return x + 1

increment_v2 = lambda x: x+1 
def h_O_f(x, func):
    return x + func(x)

h_o_f_v2 = lambda x, func: x + func(x)
result = h_O_f(2, increment)

print(result)

result = h_o_f_v2(2, increment_v2)
print(result)

result = h_o_f_v2(2, lambda x: x * 3)
print(result)

