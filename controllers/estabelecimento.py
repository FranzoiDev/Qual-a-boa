from flask import Blueprint, jsonify, request
from models import db
from models.estabelecimento import Estabelecimento
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

estabelecimento_bp = Blueprint('estabelecimento', __name__)

# Geolocalizador (Nominatim)
geolocator = Nominatim(user_agent="qual_a_boa_api")

estabelecimento_bp = Blueprint('estabelecimento', __name__)

@estabelecimento_bp.route('/', methods=['GET'])
def listar_restaurantes():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        restaurantes = Estabelecimento.query.filter(
            Estabelecimento.uf == 'PR',
            Estabelecimento.municipio == 7691
        ).paginate(page=page, per_page=per_page, error_out=False)

        # Monta a resposta
        resultado = [
            {
                'cnpj': r.cnpj,
                'nome_fantasia': r.nome_fantasia,
                'cep': r.cep,
                'uf': r.uf,
                'municipio': r.municipio
            } for r in restaurantes.items
        ]

        return jsonify({
            'restaurantes': resultado,
            'total': restaurantes.total,
            'paginas': restaurantes.pages,
            'pagina_atual': restaurantes.page
        }), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@estabelecimento_bp.route('/<cnpj>', methods=['GET'])
def detalhar_restaurante(cnpj):
    try:
        restaurante = Estabelecimento.query.filter_by(
            cnpj=cnpj,
            uf='PR',
            municipio='7691'
        ).first()

        if not restaurante:
            return jsonify({'erro': 'Restaurante não encontrado'}), 404

        resultado = {
            'cnpj': restaurante.cnpj,
            'nome_fantasia': restaurante.nome_fantasia,
            'matriz_filial': restaurante.matriz_filial,
            'situacao_cadastral': restaurante.situacao_cadastral,
            'data_situacao_cadastral': restaurante.data_situacao_cadastral,
            'data_inicio_atividades': restaurante.data_inicio_atividades,
            'cnae_fiscal': restaurante.cnae_fiscal,
            'cnae_fiscal_secundaria': restaurante.cnae_fiscal_secundaria,
            'tipo_logradouro': restaurante.tipo_logradouro,
            'logradouro': restaurante.logradouro,
            'numero': restaurante.numero,
            'complemento': restaurante.complemento,
            'bairro': restaurante.bairro,
            'cep': restaurante.cep,
            'uf': restaurante.uf,
            'municipio': restaurante.municipio,
            'ddd1': restaurante.ddd1,
            'telefone1': restaurante.telefone1,
            'ddd2': restaurante.ddd2,
            'telefone2': restaurante.telefone2,
            'correio_eletronico': restaurante.correio_eletronico
        }

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    
@estabelecimento_bp.route('/<cnpj>/localizacao', methods=['GET'])
def obter_localizacao_restaurante(cnpj):
    try:
        restaurante = Estabelecimento.query.filter_by(
            cnpj=cnpj,
            uf='PR',
            municipio='7691'
        ).first()

        if not restaurante:
            return jsonify({'erro': 'Restaurante não encontrado em Maringá'}), 404

        # Obtém o CEP do restaurante
        cep = restaurante.cep
        if not cep:
            return jsonify({'erro': 'CEP não disponível para este restaurante'}), 400

        via_cep_url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta_cep = requests.get(via_cep_url).json()

        if 'erro' in resposta_cep:
            return jsonify({'erro': 'CEP inválido ou não encontrado'}), 400

        # Monta o endereço para geolocalização
        endereco = f"{resposta_cep['logradouro']}, {resposta_cep['bairro']}, Maringá, PR, Brasil"

        try:
            localizacao = geolocator.geocode(endereco)
            if not localizacao:
                return jsonify({'erro': 'Não foi possível geolocalizar o endereço'}), 400

            resultado = {
                'cnpj': restaurante.cnpj,
                'nome_fantasia': restaurante.nome_fantasia,
                'cep': restaurante.cep,
                'latitude': localizacao.latitude,
                'longitude': localizacao.longitude
            }
            return jsonify(resultado), 200

        except GeocoderTimedOut:
            return jsonify({'erro': 'Timeout ao consultar geolocalização'}), 503

    except Exception as e:
        return jsonify({'erro': str(e)}), 500