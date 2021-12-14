import sqlite3

db_file = "db.sqlite3"
db = sqlite3.connect(db_file)
cur = db.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS matiers(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS niveaux(
        id INTEGER NOT NULL PRIMARY KEY,
        nom TEXT
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
        niveau TEXT,
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
