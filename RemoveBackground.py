from RemoveBackground import remove
from PIL import Image

image_input = Image.open(r, 'C:\xampp\htdocs\Project\CollabR\Gambar\apel.jpg')
output = remove(image_input)
output.save('C:\xampp\htdocs\Project\CollabR\Ouput', r)
