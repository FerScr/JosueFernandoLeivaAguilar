from flask import Flask, jsonify
import platform
import socket
import sys

app = Flask(__name__)

@app.route('/')
def system_info():
    sistemaop = sys.platform
    sistema = platform.system()
    version = platform.win32_ver()
    ip = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()
    core = platform.processor()

    response = {
        "Estamos en": sistema,
        "Version": version,
        "Mi direccion IP es": ip,
        "Nombre_de_host": hostname,
        "Procesador": core
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
