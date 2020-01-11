from owndb import GenericDb

db = GenericDb()
db.sentenceWrite("""
    CREATE TABLE Personas (
            id serial PRIMARY KEY,
            nombre VARCHAR(120) NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            puesto VARCHAR(60) NOT NULL
        );
""")
db.closeConnection()
