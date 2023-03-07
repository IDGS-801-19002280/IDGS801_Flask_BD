from wtforms import Form, StringField, IntegerField
from wtforms import EmailField, validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('email')
