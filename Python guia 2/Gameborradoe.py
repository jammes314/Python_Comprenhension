#################################################################
###Imagenes###

from PIL import Image
#################################################################
#Introduccion

import sys
import time
space = "-"*200
linea1 = "Hola!, esta es una pequeña guia sobre como funciona el juego."
linea2= "Primero te dejaré una lista de los lugares a visitar"
#texto1.center(50)
for letra in linea1:
    print(letra, end="")
    sys.stdout.flush()
    time.sleep(0.01)
print()
for letra in linea2:
    print(letra, end="")
    sys.stdout.flush()
    time.sleep(0.1)
#print("""
#     Hola!, esta es una pequeña guia sobre como funciona el juego
#      Primero te dejaré una lista de los lugares a visitar""")

linea3 = "1) Caballerizas"
linea4 = "2) Manuelas"
linea5 = "3) Residencias Docentes"
linea6 = "4) Sala Capitular"
linea7 = "5) Chalet"
linea8 = "6) B"
linea9 = "7) Biblioteca"
linea10 = "8) Ingenio"
linea11 = "9) Multifamiliares"
linea12 = "10) Patrimoniales"
linea13 = "11) T's"
linea14 = "12) Canchas"
linea15 = "13) Bloques"
linea16 = "14) Senescyt"

lineas = [linea3,linea4,linea5,linea6,linea7,linea8,linea9,linea10,linea11,linea12,linea13,linea14,linea15,linea16]
print()
i = 0
while i < len(lineas):
    print()
    for letra in lineas[i]:
        print(letra, end="")
        sys.stdout.flush()
        time.sleep(0.1)
    i += 1


print()
print(space)
print( """
Las reglas son sencillas:
- Si quieres información sobre un lugar, simplemente escribe "ir a [lugar o simplemnte el número correspondiente a ese lugar]."
- Si quieres ver como es este lugar simplemnte  escribe "ver [lugar o número correspondiente] (esto se siempre se podrá realizar \n simempre y cuando la imagen se encuentre disponible)"
""")

#################################################################

# Introduction narration of game


print(space)
print("Welcome to Yachay-Introductory_Game")
print(space)
print(
    "Te bajas del auto de tus padres, estas junto a una gran construccion de color blanco que parece ser de la epoca de haciendas.")
print("Puedes ver varios caminos a tu alrededor")
print("Hay un mentor  cerca tuyo")
print("""
"Te aconsejo que primero te acerques al mentor"
""")
print(space)
contador  = 0
while True:
    second = input("Que quieres hacer? ")
    contador += 1

    if contador % 2 == 0 and contador != 2:
        print(space)
        print("Recuerde que siempre puede presionar [m] para mostrar el mapa")


    if second.lower() == ("acercarse al mentor"):
        print(space)
        print("el mentor te entrega un mapa [Para mirar el mapa presiona [m]   ]")
    elif second.lower() == ("m"):
        print(space)

        imagen = Image.open("/home/mh0/Desktop/Yachay/Intr. programación/Final_Project/Campus_High.png")
        imagen.show()

        print(" Para ir a un lugar, escribe [ir a + el nombre del lugar en el mapa] ")
    if second.lower() == ("ir a biblioteca") or second.lower() == "ir a 7":

        print("A estudiar se ha dicho!!")
        print(
            "Aqui puedes estudiar, la biblioteca ofrece un ambiente tranquilo, esta construido \n sobre los restos de la maquinaria que formaba parte del Ingenio")
        segunda_accion = input("Puedes explorar la biblioteca: ")
        if segunda_accion.lower() == ("ver biblioteca") or segunda_accion.lower() == ("ver 7"):

            imagen1 = Image.open("/home/mh0/Desktop/Yachay/Intr. programación/Final_Project/Biblioteca/Biblioteca_Exterior.jpeg")
            imagen1.show()

            imagen2 = Image.open("/home/mh0/Desktop/Yachay/Intr. programación/Final_Project/Biblioteca/Biblioteca_Interior(1).jpg")
            imagen2.show()

            imagen3 = Image.open(
                "/home/mh0/Desktop/Yachay/Intr. programación/Final_Project/Biblioteca/Biblioteca_Interior(2).jpg")
            imagen3.show()


    elif second.lower() == ("ir a B") or second.lower() == "ir a 6":
        print(space)
        print(
            "Las aulas b, tambien reconstruidas, tienen distitas capacidades, la b-104 de hasta 50 personas \n, mientras las otras pueden albergar hasta 30 personas, todas cuentan con acceso al internet y proyector o pantalla")
    elif second.lower() == ("ir a caballerizas") or second.lower() == "ir a 1":
        print(space)
        print(
            "Las caballerizas estan ubicadas en en la entrada de la Universidad, apenas llegues a la primera parada dentro de la universidad, no te será muy dificil encontrarlas!\n Aquí solo recibimos clases, pero con una vista hermosa. Desde aqui puedes ingresar a \n la [Sala Capitular], al [Chalet] \n o puedes conocer un nuevo punto dirigiendote a las [Manuelas]")


    elif second.lower() == ("ir a sala capitular") or second.lower() == "ir a 4":
        print(space)
        print(
            "Construida a partir de una capilla de hacienda, ahora se usa para reuniones y presentaciones.\n Tambien tienes una vista hermosa.")
    elif second.lower() == ("ir a chalet") or second.lower() == "ir a 5":
        print(space)
        print(
                "Detras de la sala capitular, hay estatuas de madera, las cuales te conduciran al [Chalet], \n la cual en algun momento fue la residencia de los hacendados.\n Ahora sirve de residencia del Rector y coordinacion de las maestrias.")

    elif second.lower() == ("ir a manuelas") or second.lower() == "ir a 2":
        print(space)
        print("Desde las manuelas puedes ingresar a las [Residencias de docentes] y a las [multifamiliares]")
        print(
            "En las manuelas puedes encontrar varios restaurantes y un minimarket. \n Sin embargo la mayoria de estos se han trasladado a los bloques.")

    elif second.lower() == ("ir a residencias docentes") or second.lower() == "ir a 3":
        print(space)
        print(
            "Aqui residien/residian los profesores de YT, alieniandose con la filosofia de crear una comunidad de investigacion.")
    elif second.lower() == ("ir a multifamiliares") or second.lower() == "ir a 9":
        print(space)
        print("Aqui en las multifamiliares, encuetras departamentos de 2,4,6 personas.")
        print("Aqui tambien hay una concha acustica (un auditorio al aire libre)")
        print("Desde aqui puedes ir a las residencias [patrimoniales] y a las [T's] . ")

    elif second.lower() == ("ir a patrimoniales") or second.lower() == "ir a 10":
        print(space)
        print(
            "Has llegado a las patrimoniales. Son residencias reconstruidas a la viva imagen de las casas de los peones. ")
        print(
            "Estas residencias estan a media distancia de todo, un excelente lugar para vivir, si te gusta compartir. ")
        print("Aunque hasta pronto aviso no estarán habilitadas.")
        print("Por aqui tambien podras ir a las [canchas] , y a [senecyt].")

    elif second.lower() == ("ir a t's") or second.lower() == "ir a 11":
        print("Estas son las residencias mas alejadas, pero guardan un encanto singular.")
        print("En las noches, acogen la mejor vista del cielo y la ciudad de Ibarra.")

    elif second.lower() == ("ir a canchas") or second.lower() == "ir a 12":
        print(space)
        print("Aqui encontraras espacios para practicar futbol, basket, tennis y hasta calistenia")
        print("Tambien te encontraras frente a los laboratorios E2E3, los cuales son dedicados a la investigacion ")

    elif second.lower() == ("ir a senescyt") or second.lower() == "ir a 14":

        print(space)
        print(
            "En el edificio de senecyt tendras las mayorias de clases, sobre todo si te encuentras en tronco comun.")
        print(
            "Aqui tambien se encuentran las oficinas de las escuelas de la universidad y de los distintos departamentos que conforman los administrativos.")
        print("Tambien este edificio esta frente a las residencias de los [bloques] ")

    elif second.lower() == ("ir a bloques") or second.lower() == "ir a 13":
        print(space)
        print("Tambien aqui encuentas un minimarket bastante util")
        print("Gracias por ser parte de este recorrido y !!Bienvenido a Yachay!!!")
