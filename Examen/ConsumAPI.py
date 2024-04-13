import requests

url = "http://127.0.0.1:5000/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicit Exitosa')
    print("Datos: ", data)

else:
    print("Error en la solicitud: ", response.text)

