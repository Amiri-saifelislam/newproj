from typing import List
from Professeur import Professeur
from Personne import Personne
class Etudiant(Personne):
    def __init__(self, id, cne, nom, prenom, age, niveau, matieres):
        super.__init__(id, nom, prenom, age)
        self.cne     = cne
        self.niveau   = niveau
        self.matieres = matieres