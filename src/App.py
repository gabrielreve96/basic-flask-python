from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId 
from config import mongoLocal
app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = mongoLocal['RUTA_MONGO']

mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])
def crearUsuario():
    user_data = {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    }
    result = db.insert_one(user_data)
    inserted_id = str(result.inserted_id)
    response = {'message': 'Usuario creado con éxito', 'id': inserted_id}
    return jsonify(response), 201

@app.route('/users/<id>', methods=['DELETE'])
def eliminar_usuario(id):
    db.delete_one({"_id": ObjectId(id)})
    response = {'message': "Eliminado con éxito"}
    return jsonify(response), 201


@app.route('/users/<id>' , methods=["PUT"])
def actualizar_usuario(id):
    datos_actualizar={
        'name':request.json['name'],
        'email':request.json['email'],
        'password':request.json['password']
    }
    
    db.update_one({"_id": ObjectId(id)}, {"$set": datos_actualizar})
    response={"mensage":"usuario actualizaod con exito"}
    return response

if __name__ == "__main__":
    app.run(debug=True)
