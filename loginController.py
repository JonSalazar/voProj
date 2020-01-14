from app import db
from flask_hashing import Hashing
from flask import Flask
import helper
from models import Usuarios

app = Flask(__name__)
hashing = Hashing(app)

def signUp(username, password):

    salt = helper.saltGenerator(60)
    hash_value = hashing.hash_value(password, salt)
    
    usuario = Usuarios.query.filter_by(nombre=username).first()
    
    if (usuario):
        return False

    usuario = Usuarios(nombre=username, contrasena=hash_value, salt=salt)
    db.session.add(usuario)
    # db.sentenceWrite("""
    #     INSERT INTO usuarios (nombre, contrasena, salt)
    #     VALUES('%s', '%s', '%s')
    # """ % (username, hash_value, salt)
    # )
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        return False

    return True

def login(username, password):
    
    usuario = Usuarios.query.filter_by(nombre=username).first()

    # query = db.sentenceRead("""
    #     SELECT contrasena, salt FROM usuarios WHERE nombre = '%s'
    # """ % username
    # )

    if (not usuario):
        return False

    # saved_password = query[ 0 ]
    # saved_salt = query[ 1 ]
    if (not hashing.check_value(usuario.contrasena, password, usuario.salt)):
        return False

    return True