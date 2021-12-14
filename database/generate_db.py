import sqlite3

db_file = "db.sqlite3"
db = sqlite3.connect(db_file)
cur = db.cursor()

cur.execute("""
    CREATE TABLE matiers(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT
    )
""")

cur.execute("""
    CREATE TABLE niveaux(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT
    )
""")

cur.execute("""
    CREATE TABLE etudiants (
        id INTEGER NOT NULL PRIMARY KEY,
        niveau_id INTEGER,
        cne TEXT UNIQUE,
        nom TEXT,
        prenom TEXT,
        age TEXT,
        niveau TEXT,
        FOREIGN KEY(niveau_id) REFERENCES niveaux(id)
    )
""")

cur.execute("""
    CREATE TABLE professeurs (
        id INTEGER NOT NULL PRIMARY KEY,
        matier_id INTEGER,
        nom TEXT,
        prenom TEXT,
        age TEXT,
        FOREIGN KEY(matier_id) REFERENCES matiers(id)

    )
""")

cur.execute("""
    CREATE TABLE etudiants_professeurs (
        professeur_id,
        etudiant_id,
        note TEXT,
        FOREIGN KEY(professeur_id) REFERENCES professeurs(id),
        FOREIGN KEY(etudiant_id) REFERENCES etudiants(id)
    )
""")


