from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from db.connection import get_database
from models.player_schema import PlayerSchema
from pydantic import ValidationError

# Blueprint para organizar rutas
players_bp = Blueprint('players', __name__)

# Base de datos
db = get_database()
players_collection = db.players

@players_bp.route('/players', methods=['POST'])
def add_player():
    try:
        player_data = PlayerSchema(**request.get_json())  # Validar datos con Pydantic
        result = players_collection.insert_one(player_data.dict())
        return jsonify({"message": "Jugador agregado", "id": str(result.inserted_id)}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

@players_bp.route('/players', methods=['GET'])
def get_players():
    players = list(players_collection.find({}, {"_id": 1, "name": 1, "team": 1}))
    for player in players:
        player["_id"] = str(player["_id"])  # Convertimos ObjectId a string
    return jsonify(players)

@players_bp.route('/players/<id>', methods=['DELETE'])
def delete_player(id):
    result = players_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Jugador no encontrado"}), 404

    return jsonify({"message": "Jugador eliminado"})