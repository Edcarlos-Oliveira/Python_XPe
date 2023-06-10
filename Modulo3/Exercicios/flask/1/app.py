# Importação dos módulos flask e os:
import os
from flask import Flask, render_template # 'render_template' é necessário importar para trabalhar com os templates
from form import NameForm
from flask_migrate import Migrate
from models.User import db  # Modulo criado no projeto


# Primeira Parte do Projeto

# Criando um template diretório:
#template_dir = os.path.abspath('./templates')

'''# Criando o servidor:
app = Flask(__name__, template_folder=template_dir) # Adicionado a configuração 'template_folder=template_dir'

# Criando a encrepitação:
app.config['SECRET_KEY'] = 'ajsjdkdkkkekemmsfjuyeysnnshhuuenskdkdççsjjslldjj'

# Criando a rota:
@app.route('/user')
@app.route('/user/<name>') # Para a rota dinâmica
def index(name=None):
    print(name)
    return render_template('index.html', name=name) # 'name=name' para chamar no index'''

# Segunda Parte do Projeto:

'''@app.route('/', methods=['GET', 'POST']) # 'GET'(Renderiza o template), 'POST'(Envia dados do formulário)
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return render_template('index.html', name=name, form=form)'''

# Terceira Parte do Projeto:
'''app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app,db)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return render_template('index.html', name=name, form=form)'''

# Quarta Parte do Projeto:
app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app,db)

# flask db init
# flask db migrate
# flask db upgrade

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return render_template('index.html', name=name, form=form)







