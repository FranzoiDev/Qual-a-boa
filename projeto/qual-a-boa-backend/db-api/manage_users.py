from app import create_app
from app.extensions import db
from app.models.user import User

def create_user(username, email, password):
    """Cria um novo usuário de forma segura"""
    app = create_app()
    with app.app_context():
        # Verifica se o usuário já existe
        if User.query.filter_by(username=username).first():
            print(f"Erro: Usuário '{username}' já existe")
            return False
        
        if User.query.filter_by(email=email).first():
            print(f"Erro: Email '{email}' já está em uso")
            return False
        
        # Cria o novo usuário
        user = User(
            username=username,
            email=email
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        print(f"Usuário '{username}' criado com sucesso")
        return True

def list_users():
    """Lista todos os usuários"""
    app = create_app()
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def delete_user(user_id):
    """Deleta um usuário pelo ID"""
    app = create_app()
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            print(f"Usuário '{user.username}' deletado com sucesso")
            return True
        else:
            print(f"Erro: Usuário com ID {user_id} não encontrado")
            return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python manage_users.py [comando] [argumentos]")
        print("Comandos disponíveis:")
        print("  create <username> <email> <password> - Cria um novo usuário")
        print("  list - Lista todos os usuários")
        print("  delete <user_id> - Deleta um usuário")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "create":
        if len(sys.argv) != 5:
            print("Erro: Número incorreto de argumentos para create")
            print("Uso: python manage_users.py create <username> <email> <password>")
            sys.exit(1)
        create_user(sys.argv[2], sys.argv[3], sys.argv[4])
    
    elif command == "list":
        list_users()
    
    elif command == "delete":
        if len(sys.argv) != 3:
            print("Erro: Número incorreto de argumentos para delete")
            print("Uso: python manage_users.py delete <user_id>")
            sys.exit(1)
        delete_user(int(sys.argv[2]))
    
    else:
        print(f"Erro: Comando '{command}' não reconhecido")
        sys.exit(1) 