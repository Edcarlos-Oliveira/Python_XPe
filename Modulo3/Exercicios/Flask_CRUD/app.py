# Importação dos módulos:
from flask import Flask, render_template # 'render_template' é necessário importar para trabalhar com os templates
from flask_migrate import Migrate
from models.User import db  # Modulo criado no projeto
from routes.user import user_bp


# Primeira Parte do Projeto no padrão 'MVC' (Models, Views e Controllers)

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)

# Registrando a rota:
app.register_blueprint(user_bp, url_prefix='/users') # Faz o endereço da API '/users'

'''@app.route('/')
def index():
    return render_template('index.html')'''







