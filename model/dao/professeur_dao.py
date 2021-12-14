from model.bo.Professeur import Professeur
from db.db_interaction import DBInteraction

class Etudiant_dao:
    def ajouter(code,nom,prenom,age,profession):
        db = DBInteraction()
        req = f"""INSERT INTO Etudiants
        VALUES(
            {code},
            {nom},
            {prenom},
            {age},
            {profession}
        )"""
        return db.maj(req)
    
    def supprimer(id):
        db = DBInteraction()
        req = f"""DELETE FROM 'Professeurs'
        WHERE 'ID'  = {id}
        """
        return db.maj(req)