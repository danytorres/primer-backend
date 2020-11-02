from flask import Flask, jsonify, request
import conexion

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def addUser():
    try:
        if request.json['distancia'] > 4:
            datos = [
                request.json['nombre'],
                request.json['correo'],
                request.json['distancia']
            ]

            dic = {
                "nombre":datos[0],
                "correo":datos[1],
                "distancia":datos[2]
            }
            conexion.insert(dic)
            return jsonify({"message":"usuario agregado correctamente"})#, "datos": dic})
    except KeyError:
        return jsonify({"message":"no se cargaron todos los datos de nombre, correo y distancia"})
    except TypeError:
        return jsonify({"message":"no se cargo el tipo de dato correcto a las variables","tipo de dato para cada variable":{"nombre":"string","correo":"string","distancia":"integer"}})
    return jsonify({"message":"Debes de caminar mas"})

@app.route('/users')
def getUsers():
    try:
        res = []
        for usuario in conexion.traerDatos():
            res.append({"nombre":usuario['nombre'],"correo":usuario['correo'],"distancia":usuario['distancia']})
        return jsonify(res)
    except:
        return jsonify({"mensaje":"error en la carga de datos"})

if __name__ == "__main__":
    app.run(debug=True, port=4000)