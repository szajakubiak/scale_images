import os
from PIL import Image

size_full = (2160, 1440)
size_half = (1080, 720)

image_names = os.listdir("to_process")
images = []
for file_name in image_names:
    images.append(Image.open("to_process/" + file_name))

for i in range(len(images)):
    size = images[i].size
    if size[0] >= size_full[0] and size[1] >= size_full[1]:
        image = images[i].resize(size_full)
    elif size[0] >= size_half[0] and size[1] >= size_half[1]:
        image = images[i].resize(size_half)
    image.save("output/" + image_names[i])

