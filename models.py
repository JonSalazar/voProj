from app import db

class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    puesto = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return "<Id: {}>".format(self.id)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    contrasena = db.Column(db.String(120), nullable=False)
    salt = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Id: {}>".format(self.id)
