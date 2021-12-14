import sqlite3

db_file = "db.sqlite3"
db = sqlite3.connect(db_file)
cur = db.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS matiers(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS niveaux(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS etudiants (
        id INTEGER NOT NULL PRIMARY KEY,
        niveau_id INTEGER,
        cne TEXT UNIQUE,
        nom TEXT,
        prenom TEXT,
        date_of_birth TEXT,
        FOREIGN KEY(niveau_id) REFERENCES niveaux(id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS professeurs (
        id INTEGER NOT NULL PRIMARY KEY,
        matier_id INTEGER,
        nom TEXT,
        prenom TEXT,
        date_of_birth TEXT,
        FOREIGN KEY(matier_id) REFERENCES matiers(id)

    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS etudiants_professeurs (
        professeur_id,
        etudiant_id,
        note TEXT,
        FOREIGN KEY(professeur_id) REFERENCES professeurs(id),
        FOREIGN KEY(etudiant_id) REFERENCES etudiants(id)
    )
""")

cur.execute(""" insert into matiers(nom) values("english") """)
cur.execute(""" insert into matiers(nom) values("arabe") """)
cur.execute(""" insert into matiers(nom) values("francais") """)
cur.execute(""" insert into matiers(nom) values("education islamique") """)
cur.execute(""" insert into matiers(nom) values("mathematique") """)

cur.execute(""" insert into niveaux(nom) values("first grade") """)
cur.execute(""" insert into niveaux(nom) values("second grade") """)
cur.execute(""" insert into niveaux(nom) values("third grade") """)
cur.execute(""" insert into niveaux(nom) values("fourth grade") """)
cur.execute(""" insert into niveaux(nom) values("fifth grade") """)
cur.execute(""" insert into niveaux(nom) values("sixt grade") """)

cur.execute(""" insert into etudiants(niveau_id, cne, nom, prenom, date_of_birth)
        select n.id,
            "R130030312",
            "IRIZI",
            "Anass",
            "2000-08-25"
        from
            niveaux n
        where n.nom = "second grade"
        """)

cur.execute(""" insert into etudiants(niveau_id, cne, nom, prenom, date_of_birth)
        select n.id,
            "R000000000",
            "AMIRI",
            "Saif El Islam",
            "2000-1-1"
        from
            niveaux n
        where n.nom = "sixt grade"
        """)

cur.execute(""" insert into professeurs(matier_id, nom, prenom, date_of_birth)
        select m.id,
            "BEN LHOUSSAIN",
            "Larbi",
            "2000-1-1"
        from
            matiers m
        where m.nom = "arabe"
        """)

cur.execute(""" insert into professeurs(matier_id, nom, prenom, date_of_birth)
        select m.id,
            "LHOUAT",
            "Samira",
            "2000-1-1"
        from
            matiers m
        where m.nom = "francais"
        """)

cur.execute(""" insert into etudiants_professeurs (professeur_id, etudiant_id, note)
        values (1, 1, 18.3)
""")

cur.execute(""" insert into etudiants_professeurs (professeur_id, etudiant_id, note)
        values (1, 2, 10)
""")

cur.execute(""" insert into etudiants_professeurs (professeur_id, etudiant_id, note)
        values (2, 1, 18.3)
""")

cur.execute(""" insert into etudiants_professeurs (professeur_id, etudiant_id, note)
        values (2, 2, 10)
""")

cur.close()
db.close()
