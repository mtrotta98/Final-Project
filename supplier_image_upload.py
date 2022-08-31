import requests
import os

url = "http://localhost/upload"
dir = os.listdir("/home/student-03-f4a307aeef6d/supplier-data/images")
for file in dir:
  if '.jpeg' in file:
    with open("supplier-data/images/" + file, 'rb') as im:
      r = requests.pos(url, files={'file': im})