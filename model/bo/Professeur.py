from Personne import Personne
class Professeur(Personne):
    def __init__(self, id, nom, prenom, age, profession, classes):
        super.__init__(id, nom, prenom, age)
        self.profession = profession
        self.classes = classes