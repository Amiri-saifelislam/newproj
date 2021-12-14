from db.db_interaction import DBInteraction

class Professeur_dao:
    def ajouter(professeur):
        db = DBInteraction()
        req = f"""INSERT INTO Etudiants
        VALUES(
            {professeur.nom},
            {professeur.prenom},
            {professeur.age},
            {professeur.profession},
            {professeur.classes}
        )"""
        return db.maj(req)
    
    def supprimer(id):
        db = DBInteraction()
        req = f"""DELETE FROM Professeurs
        WHERE ID  = {id}
        """
        return db.maj(req)

    def modifier(professeur.id, professeurs):
        db = DBInteraction()
        req = f"""UPDATE Professeurs
                SET NOM        {professeur.nom},
                    PRENOM     {professeur.prenom},
                    AGE        {professeur.age},
                    PROFESSION {professeur.profession},
                    Classes    l+{professeur.classes}
                """
        return db.maj(req)