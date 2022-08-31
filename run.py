import os
import requests

dir = os.listdir("/home/student-03-f4a307aeef6d/supplier-data/descriptions")

for file in dir:
  with open("/home/student-03-f4a307aeef6d/supplier-data/descriptions"+file, 'r') as f:
    list_lines = f.readlines()
    dic_file = {"name": list_lines[0].split("\n")[0], 'weight': int(list_lines[1].split(' ')[0]), "description": list_lines[2].split('\n')[0], "image": file.split('.')[0] + '.jpeg'}
    response = request.post("http://localhost/fruits/"+ json=dic_file)
    print(response.status_code)
