"""
Módulo que implementa as rotas da API para gerenciamento de restaurantes.
Inclui operações CRUD e busca de restaurantes.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Restaurant
from app.utils.validators import validate_schema
from marshmallow import Schema, fields, ValidationError
import unicodedata

# Blueprint para agrupar as rotas de restaurantes
restaurants_bp = Blueprint('restaurants', __name__)

class RestaurantSchema(Schema):
    """
    Schema para validação dos dados de restaurante.
    
    Campos:
        cnpj: CNPJ do restaurante
        name: Nome do restaurante
        state: Estado onde está localizado
        city: Cidade onde está localizado
        type: Tipo de culinária/estabelecimento
        operating_hours: Horário de funcionamento
        postal_code: Código postal
        street_number: Número do endereço
    """
    cnpj = fields.String(required=True)
    name = fields.String(required=True)
    state = fields.String(required=True)
    city = fields.String(required=True)
    type = fields.String(required=True)
    operating_hours = fields.String(required=True)
    postal_code = fields.String(required=True)
    street_number = fields.String(required=True)

def normalize_text(text):
    """
    Normaliza texto removendo acentos e convertendo para minúsculas.
    
    Args:
        text (str): Texto a ser normalizado
        
    Returns:
        str: Texto normalizado
    """
    if not text:
        return ''
    # Remove acentos
    normalized = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    return normalized.lower()

@restaurants_bp.route('/', methods=['POST'])
@jwt_required()
@validate_schema(RestaurantSchema())
def create_restaurant():
    """
    Endpoint para criar um novo restaurante.
    Requer autenticação e validação dos dados.
    
    Returns:
        tuple: (JSON response, status code)
            - 201: Restaurante criado com sucesso
            - 400: CNPJ já existe
    """
    data = request.get_json()
    
    if Restaurant.query.filter_by(cnpj=data['cnpj']).first():
        return jsonify({'message': 'Restaurant with this CNPJ already exists'}), 400
    
    restaurant = Restaurant(
        cnpj=data['cnpj'],
        name=data['name'],
        state=data['state'],
        city=data['city'],
        type=data['type'],
        operating_hours=data['operating_hours'],
        postal_code=data['postal_code'],
        street_number=data['street_number']
    )
    
    db.session.add(restaurant)
    db.session.commit()
    
    return jsonify(restaurant.to_dict()), 201

@restaurants_bp.route('/', methods=['GET'])
def get_restaurants():
    """
    Endpoint para listar todos os restaurantes.
    
    Returns:
        tuple: (JSON response, status code)
            - 200: Lista de restaurantes
    """
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurants_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    """
    Endpoint para obter um restaurante específico.
    
    Args:
        id (int): ID do restaurante
        
    Returns:
        tuple: (JSON response, status code)
            - 200: Dados do restaurante
            - 404: Restaurante não encontrado
    """
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify(restaurant.to_dict()), 200

@restaurants_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@validate_schema(RestaurantSchema())
def update_restaurant(id):
    """
    Endpoint para atualizar um restaurante existente.
    Requer autenticação e validação dos dados.
    
    Args:
        id (int): ID do restaurante
        
    Returns:
        tuple: (JSON response, status code)
            - 200: Restaurante atualizado com sucesso
            - 400: CNPJ já existe
            - 404: Restaurante não encontrado
    """
    restaurant = Restaurant.query.get_or_404(id)
    data = request.get_json()
    
    # Verifica se outro restaurante já possui este CNPJ
    existing = Restaurant.query.filter_by(cnpj=data['cnpj']).first()
    if existing and existing.id != id:
        return jsonify({'message': 'Restaurant with this CNPJ already exists'}), 400
    
    restaurant.cnpj = data['cnpj']
    restaurant.name = data['name']
    restaurant.state = data['state']
    restaurant.city = data['city']
    restaurant.type = data['type']
    restaurant.operating_hours = data['operating_hours']
    restaurant.postal_code = data['postal_code']
    restaurant.street_number = data['street_number']
    
    db.session.commit()
    
    return jsonify(restaurant.to_dict()), 200

@restaurants_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_restaurant(id):
    """
    Endpoint para deletar um restaurante.
    Requer autenticação.
    
    Args:
        id (int): ID do restaurante
        
    Returns:
        tuple: (JSON response, status code)
            - 204: Restaurante deletado com sucesso
            - 404: Restaurante não encontrado
    """
    restaurant = Restaurant.query.get_or_404(id)
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

@restaurants_bp.route('/search', methods=['GET'])
def search_restaurants():
    """
    Endpoint para buscar restaurantes com base em critérios.
    Suporta busca por nome, cidade, estado e tipo.
    
    Returns:
        tuple: (JSON response, status code)
            - 200: Lista de restaurantes que correspondem aos critérios
    """
    # Obtém e decodifica os parâmetros
    name = request.args.get('name', '').strip()
    city = request.args.get('city', '').strip()
    state = request.args.get('state', '').strip()
    type = request.args.get('type', '').strip()
    
    print(f"Raw search parameters - name: {name}, city: {city}, state: {state}, type: {type}")
    
    # Obtém todos os restaurantes primeiro
    restaurants = Restaurant.query.all()
    
    # Filtra em memória
    if name:
        name_normalized = normalize_text(name)
        restaurants = [r for r in restaurants if name_normalized in normalize_text(r.name)]
    
    if city:
        city_normalized = normalize_text(city)
        restaurants = [r for r in restaurants if city_normalized in normalize_text(r.city)]
    
    if state:
        state_normalized = normalize_text(state)
        restaurants = [r for r in restaurants if state_normalized in normalize_text(r.state)]
    
    if type:
        type_normalized = normalize_text(type)
        restaurants = [r for r in restaurants if type_normalized in normalize_text(r.type)]
    
    print(f"Found {len(restaurants)} restaurants")
    return jsonify([r.to_dict() for r in restaurants]), 200 