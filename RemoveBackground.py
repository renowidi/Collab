from RemoveBackground import remove
from PIL import Image

image_input = Image.open("disini path juga")
output = remove(image_input)
output.save("disni ganti pathnya")
