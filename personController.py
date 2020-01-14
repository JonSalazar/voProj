from app import db
from models import Personas

def addPerson(name, date, job):
    persona = Personas(nombre=name, fecha_nacimiento=date, puesto=job)
    db.session.add(persona)

    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        return False

    return persona.id

def deletePerson(id):
    persona = Personas.query.filter_by(id=id).first()
    
    if (not persona):
        return False

    db.session.delete(persona)
    db.session.commit()

    return True

def getPerson(id):
    persona = Personas.query.filter_by(id=id).first()
    
    if (not persona):
        return False

    return persona

def putPerson(id, name, date, job):
    persona = Personas.query.filter_by(id=id).first()
    
    if (not pesrona):
        return False

    if (name):
        persona.nombre = name
    if (date):
        persona.fecha_nacimiento = date
    if (job):
        persona.puest = job
    
    db.session.commit()

    return True
