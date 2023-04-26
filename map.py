from PIL import Image
image = Image.open("/home/user/Desktop/Data Engineer/Python_comprenhension/Python guia 2/campus.png")
width, height = image.size
aspect_ratio = height/width
new_width = 800
new_height = int(new_width * aspect_ratio * 0.55)
image = image.resize((new_width, new_height))
image = image.convert("L")

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

ascii_image = ""
for pixel in image.getdata():
    brightness = pixel / 255
    ascii_image += ascii_chars[int(brightness * (len(ascii_chars) - 1))]
    if len(ascii_image) % new_width == 0:
        ascii_image += "\n"

print(ascii_image)
image.show()