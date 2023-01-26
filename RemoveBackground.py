from RemoveBackground import remove
from PIL import Image

image_input = Image.open("maxresdefault.jpg")
output = remove(image_input)
output.save("foto/output")
