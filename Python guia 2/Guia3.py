# from PIL import Image

# # Cargar la imagen
# imagen = Image.open("/home/user/Desktop/Data Engineer/Python_comprenhension/Python guia 2/campus.jpg")

# # Convertir la imagen a escala de grises y ajustar el tamaño en formato ASCII
# ancho, alto = imagen.size
# nuevo_ancho = 900
# factor = nuevo_ancho/ancho
# nuevo_alto = int(alto * factor * 1) # 0.4 es un factor de escala para ajustar el alto
# imagen_ascii = imagen.convert('L').resize((nuevo_ancho, nuevo_alto))

# # Imprimir la imagen en formato ASCII en la terminal
# print(imagen_ascii)
# imagen_ascii.show()


# my_list = []



# found = False

# for i in range(len(my_list)):
#     count = 1

#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             count += 1
#             if count == 4:
#                 found = True
#                 break
#     if found:
#         break

# if found:
#     print("Tienes 40")
# else:
#     print("No tienes 40 ")



year= 2020
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)