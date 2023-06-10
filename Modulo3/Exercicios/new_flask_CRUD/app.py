# Importando os modulos necessários:
from flask import Flask, render_template
from flask_migrate import Migrate
from config import DevelopmentConfig
from models.User import db, User
from flask import Response, request
import json


# Primeira Parte do Projeto (rotas estatica e dinamicas)
'''
# Criando o appCRUD:
appCRUD = Flask(__name__)

# Criando a rota estatica:
@appCRUD.route('/')

# Definindo a função:
def index():
    return '<h1> Olá Mundo! Essa é uma rota estática.</h1> <h2>Insira na url, /user/seu nome/, e atualize a página</h2>'
    
# Criando rota dinâmica:
@appCRUD.route('/user/<name>')

def user(name):
    return f'<h1> Olá {name}! Essa é uma rota dinâmica </h1>'

if __name__ == "__main__":
    appCRUD.run(debug=True, port=5000)
'''
# Segunda Parte do Projeto (Renderizando templates com arquivo html estatico):
'''
appCRUD = Flask(__name__)

@appCRUD.route('/')
def index():
    return render_template('user.html')

if __name__ == '__main__':
    appCRUD.run(debug=True, port=5000)
'''

# Renderizando templates com arquivo html dinamico:

'''
appCRUD = Flask(__name__)

@appCRUD.route('/user/<name>')
def index(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    appCRUD.run(debug=True, port=5000)
'''
app = Flask(__name__)

app.config.from_object(DevelopmentConfig())

db.init_app(app)

migrate = Migrate(app, db)


'''@app.route('/')
def index():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=DevelopmentConfig.DEBUG, port=DevelopmentConfig.PORT_HOST)'''

# Rota para listar todos os usuários:
@app.route('/user/getall')
def getALL():
    session = db.session()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(users_json))

# Rota para adicionar usuários:
@app.route('/user/create', methods=['POST'])
def create():
    body = request.get_json()
    session = db.session()
    try:
        user = User(nome=body['nome'], telefone=body['telefone'], email=body['email'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {'ERRO':'Não conseguimos gravar o usuário'}
    finally:
        session.close()

# Rota para alterar usuários:
@app.route('/user/update/<int:user_id>', methods=['PUT'])
def update(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)
        if body and body['nome']:
            user.nome = body['nome']
        if body and body['telefone']:
            user.telefone = body['telefone']
        if body and body['email']:
            user.email = body['email']
        session.commit()
        return {'OK': 'Usuário modificado com SUCESSO!'}
    except Exception as e:
        session.rollback()
        return {'ERRO': 'Usuário não modificado!'}
    finally:
        session.close()

# Rota para deletar usuário:
@app.route('/user/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return {'OK': 'Usuário DELETADO com sucesso!'}
    except Exception as e:
        session.rollback()
        return {'ERRO': 'Usuário NÃO deletado!'}
    finally:
        session.close()






