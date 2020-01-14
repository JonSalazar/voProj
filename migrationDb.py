from owndb import GenericDb

db = GenericDb()
db.sentenceWrite("""
    CREATE TABLE IF NOT EXISTS personas (
            id serial PRIMARY KEY,
            nombre VARCHAR(120) NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            puesto VARCHAR(60) NOT NULL
        );
    CREATE TABLE IF NOT EXISTS usuarios (
            id serial PRIMARY KEY,
            nombre_usuario VARCHAR(120) UNIQUE NOT NULL,
            contrasena VARCHAR(120) NOT NULL,
            salt VARCHAR(120) NOT NULL
        );
""")
db.closeConnection()
