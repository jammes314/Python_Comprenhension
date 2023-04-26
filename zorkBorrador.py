from PIL    import Image


loop = 4
print("---------------------------------------------------------")
print("Bienvenido a  ''Primer dia en Yachay''   - El juego introductorio para estudiantes de nuevo ingreso.")

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
		elif second.lower() == ("Ir a inopolis"):
			print("---------------------------------------------------------")
			print("Innopolis esta algo lejos, ve a una parada de buses y camionetas primero")

		elif second.lower() == ("Inspeccionar Aqui"):
			print("---------------------------------------------------------")
			print("Esta es la biblioteca")
		elif second.lower() == ("m"):
			print("---------------------------------------------------------")
			print("Al abrir el mapa te encuentras con los lugares a donde te puedes dirigir en la universidad.")
			imagen = Image.open("/home/user/Desktop/Data Engineer/Python_comprenhension/Python guia 2/biblio.jpg")
			ancho, alto = imagen.size
			nuevo_ancho = 500
			factor = nuevo_ancho/ancho 
			nuevo_alto = int(alto * factor*1)
			print(imagen_ascii)
			imagen_ascii.show()
	
		elif second.lower() == ("go southwest"):
			loop = 8
		
		else:
			print("---------------------------------------------------------")
	
	# Southwest Loop
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
			forest_inp = input("What do you do? ")

		if forest_inp.lower() == ("go west"):
			print("---------------------------------------------------------")
			print("You would need a machete to go further west.")
		elif forest_inp.lower() == ("go north"):
			print("---------------------------------------------------------")
			print("The forest becomes impenetrable to the North.")
		elif forest_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("Storm-tossed trees block your way.")
		elif forest_inp.lower() == ("go east"):
			loop = 9
		else:
			print("---------------------------------------------------------")
	

	# East Loop and Grating Input
	while loop == 9:
		if loop == 9:
			print("---------------------------------------------------------")
			print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
			print("There is an open grating, descending into darkness.")
			grating_inp = input("What do you do? ")

		if grating_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("You see a large ogre and turn around.")
		elif grating_inp.lower() == ("descend grating"):
			loop = 10
		else:
			print("---------------------------------------------------------")	


	# Grating Loop and Cave Input
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("You are in a tiny cave with a dark, forbidding staircase leading down.")
			print("There is a skeleton of a human male in one corner.")
			cave_inp = input("What do you do? ")

		if cave_inp.lower() == ("descend staircase"):
			loop = 11
		elif cave_inp.lower() == ("take skeleton"):
			print("---------------------------------------------------------")
			print("Why would you do that? Are you some sort of sicko?")
		elif cave_inp.lower() == ("smash skeleton"):
			print("---------------------------------------------------------")
			print("Sick person. Have some respect mate.")
		elif cave_inp.lower() == ("light up room"):
			print("---------------------------------------------------------")
			print("You would need a torch or lamp to do that.")
		elif cave_inp.lower() == ("break skeleton"):
			print("---------------------------------------------------------")
			print("I have two questions: Why and With What?")
		elif cave_inp.lower() == ("go down staircase"):
			loop = 11
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		elif cave_inp.lower() == ("suicide"):
			print("---------------------------------------------------------")
			print("You throw yourself down the staircase as an attempt at suicide. You die.")
			print("---------------------------------------------------------")
			suicide_inp = input("Do you want to continue? Y/N ")
			if suicide_inp.lower() == ("n"):
				exit()
			if suicide_inp.lower() == ("y"):
				loop = 4
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		else:
			print("---------------------------------------------------------")


	# End of game
	while loop == 11:
		if loop == 11:
			print("---------------------------------------------------------")
			print("You have entered a mud-floored room.")
			print("Lying half buried in the mud is an old trunk, bulging with jewels.")
			last_inp = input("What do you do? ")

		if last_inp.lower() == ("open trunk"):
			print("---------------------------------------------------------")
			print("You have found the Jade Statue and have completed your quest!")
		else:
			print("---------------------------------------------------------")
		
		# Exit loop at the end of game
		exit_inp = input("Do you want to continue? Y/N ")
		if exit_inp.lower() == ("n"):
			exit()
		if exit_inp.lower() == ("y"):
			loop = 4