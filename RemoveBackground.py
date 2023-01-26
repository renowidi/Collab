from RemoveBackground import remove
from PIL import Image

image_input = Image.open("gambar/gambar1.jpg")
output = remove(image_input)
output.save("Ouput")
