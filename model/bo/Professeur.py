from Personne import Personne
class Professeur(Personne):
    def __init__(self, id, nom, prenom, date_of_birth, profession, classes):
        super.__init__(id, nom, prenom, date_of_birth)
        self.profession = profession
        self.classes    = classes
