from models import db

class Empresa(db.Model):
    __tablename__ = 'empresas'
    
    cnpj_basico = db.Column(db.String(8), primary_key=True)
    razao_social = db.Column(db.String(200))
    natureza_juridica = db.Column(db.String(4))
    qualificacao_responsavel = db.Column(db.String(2))
    porte_empresa = db.Column(db.String(2))
    ente_federativo_responsavel = db.Column(db.String(50))
    capital_social = db.Column(db.Numeric(18, 2))

    def __repr__(self):
        return f'<Empresa {self.razao_social}>'