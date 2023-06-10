# Módulos para criação do formulário:
from flask_wtf import FlaskForm              # Classes que serão usadas nos formulários
from wtforms import StringField, SubmitField # Os campos para o formulário
from wtforms.validators import DataRequired  # Os validadores


# Criando uma classe para receber 'FlaskForm':
class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()]) # Necessário o validador 
    submit = SubmitField('submit')

