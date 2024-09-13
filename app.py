from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta para obtener información de un personaje
@app.route('/character', methods=['POST'])
def get_character():
    # Obtener los datos de la solicitud
    data = request.get_json()

    # Verificar si el campo 'character_id' está presente en la solicitud
    if not data or 'character_id' not in data:
        return jsonify({"error": "character_id is required"}), 400

    # Obtener el ID del personaje
    character_id = data['character_id']

    # URL de la API de Rick and Morty
    url = f'https://rickandmortyapi.com/api/character/{character_id}'

    # Realizar la solicitud a la API de Rick and Morty
    response = requests.get(url)

    # Verificar si el personaje existe
    if response.status_code == 404:
        return jsonify({"error": "Character not found"}), 404

    # Si la respuesta es exitosa, extraer el nombre y el estado del personaje
    if response.status_code == 200:
        character_data = response.json()
        return jsonify({
            "name": character_data['name'],
            "status": character_data['status']
        }), 200

    # Si ocurre algún otro error
    return jsonify({"error": "An error occurred"}), 500


# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
