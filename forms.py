from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms import EmailField 
from wtforms import validators

class UserForm (Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message='campo es requerido'), 
        validators.length(min=4, max=10, message='ingrese un nombre valido')
    ])
    email = EmailField('correo', [validators.Email(message='ingrese un correo valido')])
    apaterno = StringField('apaterno')
    materias = SelectField(choices=[('Español', 'Esp', ), ('Mat', 'Matematicas'), ('Ingles', 'ING')])
    edad = IntegerField('edad', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])
    #radios = RadioField('Curso', choices=[('1', '1'), ('2', '2'), ('3', '3')])
