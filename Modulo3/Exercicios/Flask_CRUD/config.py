# Importando o modulo 'os':
import os

# Recebe um número randômico com 32 caracteres
SECRET_KEY = os.urandom(32) 

# Criação de um diretório base
basedir = os.path.abspath(os.path.dirname(__file__)) 

# Para eventuais avisos do framework
DEBUG = True 

# local de hospedagem do banco de dados ('sqlite')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db') 

SQLALCHEMY_TRACK_MODIFICATIONS = False

