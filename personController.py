from owndb import GenericDb

class PersonController:

    def __init__(self):
        self.db = GenericDb()

    def add_person(self, name, date, job):
        self.db.sentenceWrite("INSERT INTO Personas (nombre, fecha_nacimiento, puesto) VALUES ('%s', '%s', '%s')" % (name, date, job))

    def delete_person(self, name):
        self.db.sentenceWrite("DELETE FROM Personas WHERE nombre='%s'" % name)
    
    def get_person(self, name):
        rows = self.db.sentenceRead("SELECT nombre, fecha_nacimiento, puesto FROM Personas WHERE nombre='%s'" % name)
        return rows

    def put_person(self, current_name, name, date, job):
        self.db.sentenceWrite("""
            UPDATE Personas SET nombre='%s', fecha_nacimiento='%s', puesto='%s' WHERE nombre='%s'
        """ % (name, date, job, current_name))