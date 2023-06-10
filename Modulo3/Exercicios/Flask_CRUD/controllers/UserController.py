from flask import Response, request
from models.User import User
from flask_sqlalchemy import SQLAlchemy
import json

# Criar a inicialização do banco de dados:
db = SQLAlchemy()


# Criando a função do index:
def index():
    session = db.session() # Abrindo a sessão
    users = session.query(User).all()   
    users_json = [user.serialize() for user in users]
    session.close() # Fechando a sessão
    return Response(json.dumps(users_json))

# Criando nova rota para 'create':
def store():
    body = request.get_json()
    session = db.session()
    try:
        user = User(name=body['name'], age=body['age'], address=body['address'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback() # 'rollback' bloqueia o 'session' de continuar
        return {'ERRO':'Não conseguimos gravar o usuário'}
    finally:
        session.close() # Fecha a sessão

def show(user_id):
    session = db.session()
    try:
        user = session.query(User.get(user_id))
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {'ERRO':'Não conseguimos retornar com o usuário'}
    finally:
        session.close()

def update(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)

        if body and body['name']:
            user.name = body['name']
        if body and body['age']:
            user.age = body['age']
        if body and body['address']:
            user.address = body['address']
        session.commit()
        return {'OK':'Conseguimos atualizar o usuário'}
    except Exception as e:
        session.rollback()
        return {'ERRO':'Não conseguimos atualizar o usuário'}
    finally:
        session.close()

def destroy(user_id):
    session = db.session()
    try:
        user = session.query(User).get[user_id]
        session.delete(user)
        session.commit()
        return {'OK':'Conseguimos deletar o usuário'}
    except Exception as e:
        session.rollback()
        return {'ERRO':'Não conseguimos deletar o usuário'}
    finally:
        session.close()










