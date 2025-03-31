from flask import Flask
from config import Config
from models import db, init_app
from controllers.estabelecimento import estabelecimento_bp
from controllers.empresa import empresa_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o db com o app
init_app(app)

# Registra os blueprints
app.register_blueprint(estabelecimento_bp, url_prefix='/estabelecimentos')
app.register_blueprint(empresa_bp, url_prefix='/empresas')

@app.route('/')
def teste():
    return "API funcionando!"

if __name__ == '__main__':
    app.run(debug=True)