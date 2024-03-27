import json

file_name = "data.json"

with open(file_name) as data:
    datos = json.load(data)

print('\n'.join([f"{key}: {value[0]}" if key == "version" else f"{key}: {value}" for key, value in datos.items()]))
