# dict = {}
# for i in range(1, 5):
#     dict[i] = i * 2 
# print(dict)


# dict_2 = { i: i*2 for  i  in range(1,5)}

# print(dict_2)


# import random
# countries = ['col' , 'mex' , 'us' , 'ec']

# population = {}
# for country in countries:
#     population[country] = random.randint(5, 100)
# print(population)


# population_2 = {country: random.randint(5, 100) for country in countries}
# print(population_2)

# result = {country: population for (country, population) in population_2.items() if population> 10}
# print(result)
# names  = ['nico', 'zule', 'santi']
# ages = [12, 15, 98]

# new_dict = {names[i]: ages[i] for i in range(len(names))}
# print(new_dict)
# import random
# countries = ['col' , 'mex' , 'us' , 'ec']
# populationV2 = {country: random.randint(5, 100) for country in countries}
# print(populationV2)

# result= {country: population for (country, population) in populationV2.items() if population > 20}
# print(result)

text = 'Hola, estoy aprendiendo a programar'
unique = {car: text.count(car) for car in text if car in 'aeiou'  }
print(unique)
