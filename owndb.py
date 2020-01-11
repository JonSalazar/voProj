import psycopg2

class GenericDb:

    def __init__(self):
        self.able = False
        try:
            connect_str = "dbname='postgres' user='postgres' host='localhost' " + \
                    "password='pass123'"
            # use our connection values to establish a connection
            self._conn = psycopg2.connect(connect_str)
            # create a psycopg2 cursor that can execute queries
            self._cursor = self._conn.cursor()
            self.able = True
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)

    def sentenceRead(self, query):
        if (not self.able):
            return
        # execute query directly CHANGE THIS AS SOON AS POSSIBLE
        self._cursor.execute(query)
        self._conn.commit()
        rows = self._cursor.fetchone()
        return rows
    
    def sentenceWrite(self, query):
        if (not self.able):
            return
        # execute query directly CHANGE THIS AS SOON AS POSSIBLE
        self._cursor.execute(query)
        self._conn.commit()

    def closeConnection(self):
        if (not self.able):
            return
        self._cursor.close()
        self._conn.close()
