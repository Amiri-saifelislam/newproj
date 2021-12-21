import sqlite3

db = sqlite3.connect("db.sqlite3",
                     detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = db.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS niveaux (
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
        date_de_naissance DATE,
        FOREIGN KEY(niveau_id) REFERENCES niveaux(id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS professions (
        id INTEGER NOT NULL PRIMARY KEY
        nom TEXT UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS professeurs (
        id INTEGER NOT NULL PRIMARY KEY,
        profession_id INTEGER,
        nom TEXT,
        prenom TEXT,
        date_de_naissance DATE,
        FOREIGN KEY(profession_id) REFERENCES professions(id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS matiers (
        professeur_id INTEGER,
        etudiant_id INTEGER,
        note INTEGER,
        FOREIGN KEY(professeur_id) REFERENCES professeurs(id),
        FOREIGN KEY(etudiant_id) REFERENCES etudiants(id)
    )
""")

cur.execute(""" insert into professions(nom) values("english") """)
cur.execute(""" insert into professions(nom) values("arabe") """)
cur.execute(""" insert into professions(nom) values("francais") """)
cur.execute(""" insert into professions(nom) values("education islamique") """)
cur.execute(""" insert into professions(nom) values("mathematique") """)

cur.execute(""" insert into niveaux(nom) values("first grade") """)
cur.execute(""" insert into niveaux(nom) values("second grade") """)
cur.execute(""" insert into niveaux(nom) values("third grade") """)
cur.execute(""" insert into niveaux(nom) values("fourth grade") """)
cur.execute(""" insert into niveaux(nom) values("fifth grade") """)
cur.execute(""" insert into niveaux(nom) values("sixt grade") """)

cur.execute(""" insert into etudiants(niveau_id, cne, nom, prenom, date_de_naissance)
        select n.id,
            "R130030312",
            "IRIZI",
            "Anass",
            "2000-08-25"
        from
            niveaux n
        where n.nom = "second grade"
        """)

cur.execute(""" insert into etudiants(niveau_id, cne, nom, prenom, date_de_naissance)
        select n.id,
            "R000000000",
            "AMIRI",
            "Saif El Islam",
            "2000-1-1"
        from
            niveaux n
        where n.nom = "sixt grade"
        """)

cur.execute(""" insert into professeurs(profession_id, nom, prenom, date_de_naissance)
        select p.id,
            "BEN LHOUSSAIN",
            "Larbi",
            "2000-1-1"
        from
            professions p
        where p.nom = "arabe"
        """)

cur.execute(""" insert into professeurs(profession_id, nom, prenom, date_de_naissance)
        select p.id,
            "LHOUAT",
            "Samira",
            "2000-1-1"
        from
            professions p
        where p.nom = "francais"
        """)

cur.execute(""" insert into matiers (professeur_id, etudiant_id, note)
        values (1, 1, 18.3)
""")

cur.execute(""" insert into matiers (professeur_id, etudiant_id, note)
        values (1, 2, 10)
""")

cur.execute(""" insert into matiers (professeur_id, etudiant_id, note)
        values (2, 1, 18.3)
""")

cur.execute(""" insert into matiers (professeur_id, etudiant_id, note)
        values (2, 2, 10)
""")

cur.execute("""select * from etudiants where id = 1""")
print(cur.fetchall())

cur.execute("""select * from professeurs""")
print(cur.fetchall())

cur.execute("""select * from etudiants where 1 = 2""")
print(cur.fetchall())

cur.execute("""select * from etudiants where 1 = 2""")
print(cur.fetchone())

cur.execute("""select * from etudiants""")
print(cur.fetchone())

db.commit()
cur.close()
db.close()
