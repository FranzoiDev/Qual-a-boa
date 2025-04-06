"""
Módulo que define o modelo de Usuário para o banco de dados.
Implementa funcionalidades de autenticação e serialização.
"""

from app.extensions import db
import bcrypt

class User(db.Model):
    """
    Modelo que representa um usuário no sistema.
    
    Atributos:
        id: Identificador único do usuário
        username: Nome de usuário único
        email: Email único do usuário
        password_hash: Hash da senha do usuário (armazenado de forma segura)
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        """
        Define a senha do usuário, gerando um hash seguro.
        
        Args:
            password (str): Senha em texto plano a ser hasheada
        """
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.
        
        Args:
            password (str): Senha em texto plano a ser verificada
            
        Returns:
            bool: True se a senha estiver correta, False caso contrário
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self):
        """
        Converte o objeto usuário para um dicionário, excluindo informações sensíveis.
        
        Returns:
            dict: Representação do usuário em formato dicionário
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        } 