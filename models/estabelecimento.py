from models import db

class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimentos_filtrados'
    
    cnpj_basico = db.Column(db.String(8))
    cnpj_ordem = db.Column(db.String(4))
    cnpj_dv = db.Column(db.String(2))
    matriz_filial = db.Column(db.String(1))
    nome_fantasia = db.Column(db.String(200))
    situacao_cadastral = db.Column(db.String(2))
    data_situacao_cadastral = db.Column(db.String(8))
    motivo_situacao_cadastral = db.Column(db.String(2))
    nome_cidade_exterior = db.Column(db.String(200))
    pais = db.Column(db.String(3))
    data_inicio_atividades = db.Column(db.String(8))
    cnae_fiscal = db.Column(db.String(7))
    cnae_fiscal_secundaria = db.Column(db.String(1000))
    tipo_logradouro = db.Column(db.String(20))
    logradouro = db.Column(db.String(200))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(200))
    bairro = db.Column(db.String(200))
    cep = db.Column(db.String(8))
    uf = db.Column(db.String(2))
    municipio = db.Column(db.String(4))
    ddd1 = db.Column(db.String(4))
    telefone1 = db.Column(db.String(8))
    ddd2 = db.Column(db.String(4))
    telefone2 = db.Column(db.String(8))
    ddd_fax = db.Column(db.String(4))
    fax = db.Column(db.String(8))
    correio_eletronico = db.Column(db.String(200))
    situacao_especial = db.Column(db.String(200))
    data_situacao_especial = db.Column(db.String(8))
    cnpj = db.Column(db.String(14), primary_key=True)

    def __repr__(self):
        return f'<Estabelecimento {self.nome_fantasia}>'