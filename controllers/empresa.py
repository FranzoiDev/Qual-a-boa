from flask import Blueprint, jsonify, request
from models import db
from models.empresa import Empresa

empresa_bp = Blueprint('empresa', __name__)

@empresa_bp.route('/empresas', methods=['GET'])
def listar_empresas():
    try:
        razao_social = request.args.get('razao_social', type=str)

        query = db.session.query(Empresa).with_entities(
            Empresa.cnpj_basico,
            Empresa.razao_social,
            Empresa.porte_empresa
        )

        if razao_social:
            query = query.filter(Empresa.razao_social.ilike(f'%{razao_social}%'))

        empresas = query.order_by(Empresa.cnpj_basico).limit(1000).all()

        # Monta a resposta
        resultado = [
            {
                'cnpj_basico': e.cnpj_basico,
                'razao_social': e.razao_social,
                'porte_empresa': e.porte_empresa
            } for e in empresas
        ]

        proximo_cnpj = empresas[-1].cnpj_basico if empresas else None

        return jsonify({
            'empresas': resultado,
            'proximo_cnpj': proximo_cnpj
        }), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@empresa_bp.route('/empresas/<cnpj_basico>', methods=['GET'])
def detalhar_empresa(cnpj_basico):
    try:
        empresa = Empresa.query.filter_by(cnpj_basico=cnpj_basico).first()

        if not empresa:
            return jsonify({'erro': 'Empresa não encontrada'}), 404

        resultado = {
            'cnpj_basico': empresa.cnpj_basico,
            'razao_social': empresa.razao_social,
            'natureza_juridica': empresa.natureza_juridica,
            'qualificacao_responsavel': empresa.qualificacao_responsavel,
            'porte_empresa': empresa.porte_empresa,
            'ente_federativo_responsavel': empresa.ente_federativo_responsavel,
            'capital_social': float(empresa.capital_social) if empresa.capital_social else None
        }

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500