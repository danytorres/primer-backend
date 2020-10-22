from flask import Flask, jsonify, request
import conexion

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def addUser():
    if request.json['distancia'] > 4:
        datos = [
            request.json['nombre'],
            request.json['correo'],
            request.json['distancia']
        ]
        conexion.insert(datos)
        dic = {
            "nombre":datos[0],
            "correo":datos[1],
            "distancia":datos[2]
        }
        return jsonify({"message":"usuario agregado correctamente", "datos": dic})
    return jsonify({"message":"Debes de caminar mas"})

@app.route('/users')
def getUsers():
    res = []
    for usuario in conexion.traerDatos():
        dic = {"nombre":usuario[0],"correo":usuario[1],"distancia":usuario[2]}
        res.append(dic)
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=4000)