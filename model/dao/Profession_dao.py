from model.bo.Profession import Profession
from model.dao.db.db_interaction import DBInteraction

class Profession_dao:
    def ajouter(profession):
        req = """INSERT INTO professions (nom)
        values (?)"""

        db = DBInteraction()
        db.maj(req, profession.nom)
        
        req = """SELECT *
        FROM professions
        WHERE nom = ?"""
        result_set = db.requete(req, profession.nom)
        profession.id = result_set[0][0]
    
    def chercher(id):
        req = """SELECT *
        FROM professions
        WHERE id = ?"""

        db = DBInteraction()
        result_set = db.requete(req, id)
        if len(result_set) != 0:
            result = Profession(result_set[0][0], result_set[0][1])
            return result

        return None
            

    def maj(profession):
        req = """UPDATE professions
        SET nom = ?
        WHERE id = ?"""

        db = DBInteraction()
        db.maj(req, profession.nom, profession.id)

    def supprimer(profession):
        req = """DELETE FROM professions
        WHERE id = ?"""

        db = DBInteraction()
        db.maj(req, profession.id)