import sqlite3
BASE_DE_DONNES = "db.sqlite"

class DBInteraction :
    def __init__(self):
        self.conn = sqlite3.connect(BASE_DE_DONNES)
        self.cur  = self.conn.cursor()

    def requete(self,req):
        self.cur.execute(req)
        return self.cur.fetchall()

    def maj(self,req):
        self.cur.execute(req)
        con.commit()
        return self.cur.rowcount

    def __del__(self):
        self.cur.close()
        self.conn.close()




