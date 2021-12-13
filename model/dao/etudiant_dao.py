from model.bo.Etudiant import Etudiant
from db.db_interaction import DBInteraction

class Etudiant_dao:
    def ajouter(code,nom,prenom,age,niveau):
        db = DBInteraction()
        req = f"""INSERT INTO Etudiants
        VALUES(
            {code},
            {nom},
            {prenom},
            {age},
            {niveau}
        )"""
        return db.maj(req)
