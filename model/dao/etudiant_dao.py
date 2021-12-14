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
        db.maj(req)
        req = f""" SELECT id
            FROM etudiants
            WHERE cne = {etudiant.cne}
        """

    
    def supprimer(etudiant):
        db = DBInteraction()
        req = f"""DELETE FROM Etudiants
        WHERE ID  = {id}
        """
        return db.maj(req)
