from PIL import Image
import os

dir = os.listdir("/home/student-03-f4a307aeef6d/supplier-data/images")

for file in dir:
  if 'tiff' in file:
    im = Image.open("/home/student-03-f4a307aeef6d/supplier-data/images/" + file)
    im.convert("RGB").resize((600,400)).save("supplier-data/images/" + file.split('.')[0] + '.jpeg', 'JPEG')
