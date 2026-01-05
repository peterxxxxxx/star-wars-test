import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from models import db, Character

# Cargar configuración del .env
load_dotenv()

app = Flask(__name__)
CORS(app) # Importante para que el Frontend se conecte después

# Configuración de la base de datos de Neon
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/api/characters', methods=['GET'])
def get_characters():
    # Parámetros de la Fase 1: Paginación y Búsqueda
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    search = request.args.get('search', '', type=str)

    # Consulta base
    query = Character.query

    # Sistema de Filtrado (Fase 1)
    if search:
        query = query.filter(Character.name.ilike(f"%{search}%"))

    # Ejecutar Paginación
    pagination = query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": page,
        "characters": [c.to_dict() for c in pagination.items]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)