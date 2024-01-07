
class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        print("Hello")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


personne = Personne()
personne.afficherAge()

eleve = Eleve()
eleve.afficherAge()
