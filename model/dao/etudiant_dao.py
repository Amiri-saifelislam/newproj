from db.db_interaction import DBInteraction

class Etudiant_dao:
    def ajouter(etudiant):
        db = DBInteraction()
        req = f"""INSERT INTO Etudiants
        VALUES(
            {etudiant.cne},
            {etudiant.nom},
            {etudiant.prenom},
            {etudiant.age},
            {etudiant.niveau}
        )"""
        return db.maj(req)
    
    def supprimer_byid(id):
        db = DBInteraction()
        req = f"""DELETE FROM Etudiants
        WHERE ID  = {id}
        """
        return db.maj(req)
    def modifdier():