from flask_sqlalchemy import SQLAlchemy

# Criação do modulo:
db = SQLAlchemy()

# Criação da classe do modulo:
class User(db.Model):
    __tablename__ = 'users' # Define o nome da tabela
    id = db.Column(db.Integer, primary_key=True) # Cria o 'id' e chave primária
    name = db.Column(db.String(30))
    age = db.Column(db.String(30))
    address = db.Column(db.String(120))

# Criação do objeto:
def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'address': self.address
    }
