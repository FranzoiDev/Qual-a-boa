"""
Módulo que define o modelo de Restaurante para o banco de dados.
Implementa a estrutura de dados e serialização de restaurantes.
"""

from app.extensions import db

class Restaurant(db.Model):
    """
    Modelo que representa um restaurante no sistema.
    
    Atributos:
        id: Identificador único do restaurante
        cnpj: CNPJ único do restaurante
        name: Nome do restaurante
        state: Estado onde o restaurante está localizado
        city: Cidade onde o restaurante está localizado
        type: Tipo de culinária/estabelecimento
        operating_hours: Horário de funcionamento
        postal_code: Código postal do endereço
        street_number: Número do endereço
    """
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    operating_hours = db.Column(db.String(200))
    postal_code = db.Column(db.String(9), nullable=False)
    street_number = db.Column(db.String(10), nullable=False)
    
    def to_dict(self):
        """
        Converte o objeto restaurante para um dicionário.
        
        Returns:
            dict: Representação do restaurante em formato dicionário
        """
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'name': self.name,
            'state': self.state,
            'city': self.city,
            'type': self.type,
            'operating_hours': self.operating_hours,
            'postal_code': self.postal_code,
            'street_number': self.street_number
        } 