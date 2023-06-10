from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    telefone = db.Column(db.String(15))
    email = db.Column(db.String(30))

    def serialize(self):
        return {'id': self.id, 'Nome': self.nome, 'Telefone': self.telefone, 'Email': self.email}
    