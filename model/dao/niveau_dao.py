from model.bo.Niveau import Niveau
from model.dao.db.db_interaction import DBInteraction

class Niveau_dao:
    def ajouter(niveau):
        req = """INSERT INTO niveaux (nom)
        values (?)"""

        db = DBInteraction()
        db.maj(req, niveau.nom)
        
        req = """SELECT *
        FROM niveaux
        WHERE nom = ?"""
        result_set = db.requete(req, niveau.nom)
        niveau.id = int(result_set[0][0])
    
    def chercher(id):
        req = """SELECT *
        FROM niveaux
        WHERE id = ?"""

        db = DBInteraction()
        result_set = db.requete(req, id)
        if len(result_set) != 0:
            result = Niveau(result_set[0][0], result_set[0][1])
            return result

        return None


    def maj(niveau):
        req = """UPDATE niveaux
        SET nom = ?
        WHERE id = ?"""

        db = DBInteraction()
        db.maj(req, niveau.nom, niveau.id)

    def supprimer(niveau):
        req = """DELETE FROM niveaux
        WHERE id = ?"""

        db = DBInteraction()
        db.maj(req, niveau.id)