from PIL import Image

# Introduction narration of game


loop = 4
print("---------------------------------------------------------")
print("Bienvenido a yachay.")

while True:
	# First Input Loop
	while loop == 4:
		if loop == 4:
			print("---------------------------------------------------------")
			print("Te bajas del auto de tus padres, estas junto a una gran construccion de color blanco que parece ser de la epoca de haciendas.")
			print("Puedes ver varios caminos a tu alrededor")
			print("Hay un mentor  cerca tuyo")
			second = input("Que quieres hacer? ")

		if second.lower() == ("acercarse al mentor"):
			print("---------------------------------------------------------")
			print("el mentor te entrega un mapa [Para mirar el mapa presiona [m]   ]")
		elif second.lower() == ("ir a inopolis"):
			print("---------------------------------------------------------")
			print("Inopolis esta muy lejos, ve a una parada de buses y camionetas primero.")
		elif second.lower() == ("ir a biblioteca"):
			print("---------------------------------------------------------")
			print("Esta es la biblioteca, para saber mas Escribe  [biblioteca].")
		elif second.lower() == ("m"):
			print("---------------------------------------------------------")
		
			imagen = Image.open("/home/user/Desktop/Data Engineer/Python_comprenhension/Python guia 2/mapaFinal.jpg")
			ancho, alto = imagen.size
			nuevo_ancho = 1000
			factor = nuevo_ancho/ancho
			nuevo_alto = int(alto * factor * 1)
			imagen_ascii = imagen.convert('L').resize((nuevo_ancho, nuevo_alto))
			print(imagen_ascii)
			imagen_ascii.show()
			print(" Para ir a un lugar, escribe [ir a + el nombre del lugar en el mapa] " )
		elif second.lower() == ("biblioteca"):
			print("---------------------------------------------------------")
			print("A estudiar se ha dicho!!")
			print("Aqui puedes estudiar, la biblioteca ofrece un ambiente tranquilo, esta construido \n sobre los restos de la maquinaria que formaba parte del Ingenio")
		elif second.lower() == ("ir a b"):
			print("---------------------------------------------------------")
			print("Las aulas b, tambien reconstruidas, tienen distitas capacidades, la b-104 de hasta 50 personas \n, mientras las otras pueden albergar hasta 30 personas, todas cuentan con acceso al internet y proyector o pantalla")
		elif second.lower() == ("ir a caballerisas"):
			loop = 8
		elif second.lower() == ("read leaflet"):
			print("---------------------------------------------------------")
			print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
		else:
			print("---------------------------------------------------------")
	

	# Caballerisas Loop
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("Aquí solo recibimos clases, pero con una vista hermosa. Desde aqui puedes ingresar a \n la [Sala Capitular], al [Chalet] \n o puedes conocer un nuevo punto dirigiendote a las [Manuelas]")
			forest_inp = input("Que quieres hacer? ")

		if forest_inp.lower() == ("ir a sala capitular"):
			print("---------------------------------------------------------")
			print("Construida a partir de una capilla de hacienda, ahora se usa para reuniones y presentaciones.\n Tambien tienes una vista hermosa.")
		elif forest_inp.lower() == ("ir a chalet"):
			print("---------------------------------------------------------")
			print("Detras de la sala capitular, hay estatuas de madera, las cuales te conduciran al [Chalet], \n la cual en algun momento fue la residencia de los hacendados.\n Ahora sirve de residencia del Rector y coordinacion de las maestrias.")
		elif forest_inp.lower() == ("ir a biblioteca"):
			print("---------------------------------------------------------")
			
			loop = 4
		elif forest_inp.lower() == ("ir a manuelas"):
			loop = 9
		else:
			print("---------------------------------------------------------")
	

	# East Loop and Grating Input
	while loop == 9:
		if loop == 9:
			print("---------------------------------------------------------")
			print("Desde las manuelas puedes ingresar a las [Residencias de docentes] y a las [multifamiliares]")
			print("En las manuelas puedes encontrar varios restaurantes y un minimarket. \n Sin embargo la mayoria de estos se han trasladado a los bloques.")
			grating_inp = input("Que quieres hacer? ")

		if grating_inp.lower() == ("ir a residencias docentes"):
			print("---------------------------------------------------------")
			print("Aqui residien/residian los profesores de YT, alieniandose con la filosofia de crear una comunidad de investigacion.")
		elif grating_inp.lower() == ("ir a multifamiliares"):

			loop = 10
		else:
			print("---------------------------------------------------------")	


	# Grating Loop and Cave Input
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("Aqui en las multifamiliares, encuetras departamentos de 2,4,6 personas.")
			print("Aqui tambien hay una concha acustica (un auditorio al aire libre)")
			print("Desde aqui puedes ir a las residencias [patrimoniales] y a las [T's] . ")
			cave_inp = input("Que quieres hacer? ")

		if cave_inp.lower() == ("ir a patrimoniales"):
			loop = 11
		if cave_inp.lower() == ("ir a Concha"):
			print("---------------------------------------------------------")
			print("Aqui hay reuniones que los administrativos organizan, aunque tambian hay eventos de todo tipo.")
		if cave_inp.lower() == ("ir a t's"):
			print("Estas son las residencias mas alejadas, pero guardan un encanto singular.")
			print("En las noches, acogen la mejor vista del cielo y la ciudad de Ibarra.")
		else:
			print("---------------------------------------------------------")


	# End of game
	while loop == 11:
		if loop == 11:
			print("---------------------------------------------------------")
			print("Has llegado a las patrimoniales. Son residencias reconstruidas a la viva imagen de las casas de los peones. ")
			print("Estas residencias estan a media distancia de todo, un excelente lugar para vivir, si te gusta compartir. ")
			print("Aunque hata pronto aviso no estan habilitadas.")
			print("Por aqui tambien podras ir a las [canchas] , y a [senecyt].")
			print("Animate, estas llegando al final de tu recorrido.")
			last_inp = input("Que quieres hacer? ")

		if last_inp.lower() == ("ir a canchas"):
			print("---------------------------------------------------------")
			print("Aqui encontraras espacios para practicar futbol, basket, tennis y hasta calistenia")
			print("Tambien te encontraras frente a los laboratorios E2E3, los cuales son dedicados a la investigacion ")
		if last_inp.lower() == ("ir a senecyt"):
			loop = 12
		else:
			print("---------------------------------------------------------")
	while loop == 12:
		if loop == 12:
			print("                                            ")
			print("----------------------------------------------------")
			print("Estas a punto de finalizar tu recorrido.")
			print("En el edificio de senecyt tendras las mayorias de clases, sobre todo si te encuentras en tronco comun.")
			print("Aqui tambien se encuentran las oficinas de las escuelas de la universidad y de los distintos departamentos que conforman los administrativos.")
			print("Tambien este edificio esta frente a las residencias de los [bloques] ")


		
		# Exit loop at the end of game
		exit_inp = input("Que quieres hacer")
		if exit_inp.lower() == ("ir a bloques"):
			print("                                            ")
			print("----------------------------------------------------")
			print("Esta es tu ultima parada, estas residencias acogedoras las encuentras para 2,  y hasta 6 personas.")
			print("Tambien aqui encuentas un minimarket bastante util")
			print("Gracias por ser parte de este recorrido y !!Bienvenido a Yachay!!!")
			exit()
		