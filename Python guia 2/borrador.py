
edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

intervalos = [(10, 13), (13, 16), (16, 19), (19, 22)]

edadesOrdenadas = sorted(edades)
print(edadesOrdenadas)

NumIntervals = int(input('How many intervals do you want: '))

R = max(edades) - min(edades)
print(f'Rago = {R}')

Amplitude = R/NumIntervals
print(f'La amplitud es: {Amplitude}')





intervalos2 = []
def intervalosss(x):
  element = 0
  contador = 0

  while contador <= NumIntervals+1 :
    element += x
    intervalos2.append(element)
intervalosss(min(edades))
print(intervalos2)



Intervalos1= [(num, num+Amplitude) for num in range(min(edades), max(edades)+1)]
print(Intervalos1)

mapa_edades = dict(zip(intervalos, [0] * len(intervalos)))
print(mapa_edades)