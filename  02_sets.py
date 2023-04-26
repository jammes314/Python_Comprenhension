set_countryes = {'col', 'mex', 'bol'}
print('col' in set_countryes)


size = len(set_countryes)
print(size)

# add
set_countryes.add('pe')
print(set_countryes)


# update
set_countryes.update({'ar', 'ecua', 'pe'})
print(set_countryes)


# remove
set_countryes.remove('ar')
print(set_countryes)

#set_countryes.discard('arg')
set_countryes.discard('arg')
print(set_countryes)
set_countryes.add('arg')

print(set_countryes)

set_countryes.clear()

print(set_countryes)

print(len(set_countryes))


    # add(): Añade un elemento.

    # update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

    # discard(): Elimina un elemento y si ya existe no lanza ningún error.

    # remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

    # pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

    # clear(): Elimina todo el contenido del conjunto.

