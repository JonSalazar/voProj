from owndb import GenericDb
from flask_hashing import Hashing
from flask import Flask
import helper

db = GenericDb()
app = Flask(__name__)
hashing = Hashing(app)

def signUp(username, password):

    salt = helper.saltGenerator(60)
    hash_value = hashing.hash_value(password, salt)
    
    query = db.sentenceRead("""
        SELECT nombre_usuario FROM usuarios WHERE nombre_usuario = '%s'
    """ % username
    )

    if (query):
        return False

    db.sentenceWrite("""
        INSERT INTO usuarios (nombre_usuario, contrasena, salt)
        VALUES('%s', '%s', '%s')
    """ % (username, hash_value, salt)
    )

    return True

def login(username, password):
    query = db.sentenceRead("""
        SELECT contrasena, salt FROM usuarios WHERE nombre_usuario = '%s'
    """ % username
    )

    if (not query):
        return False

    saved_password = query[ 0 ]
    saved_salt = query[ 1 ]
    if (not hashing.check_value(saved_password, password, saved_salt)):
        return False

    return True