import MySQLdb

class SQLConnecter:
    @property
    def cursor(self):
        return self.cursor

    @property
    def connection(self):
        return self.connection

    def __init__(self):
        self.connection = MySQLdb.connect(
            host="host", user="user", passwd="passwd", db="db_name", charset="utf8"
        )
        SQLConnecter.cursor = self.connection.cursor()

    def Insert(self):
        self.cursor.execute(
            """INSERT INTO tablename (column1, column2) VALUES (%(red)s,%(blue)s)""",
            {"red": "char1", "blue": "char2"},
        )
        self.connection.commit()
        self.connection.close()

    def Update(self):
        self.cursor.execute(
            """UPDATE tablename SET column1=%(red)s, column2=%(blue)s WHERE column3=%(yellow)s""",
            {"red": "char1", "blue": "char2", "yellow": "char3"},
        )
        self.connection.commit()
        self.connection.close()

    def Select(self):
        self.cursor.execute(
            """SELECT * FROM tablename WHERE column1=? OR column2=?', ('red', 'blue')""",
        )
        print(self.cursor.fetchall())
        self.connection.commit()
        self.connection.close()
