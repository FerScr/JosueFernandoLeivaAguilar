from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"Fer", "enable":True},
    {"id":2, "nombre":"Joss", "enable":True},
    {"id":3, "nombre":"Less", "enable":True},
    {"id":4, "nombre":"Brando", "enable":False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)