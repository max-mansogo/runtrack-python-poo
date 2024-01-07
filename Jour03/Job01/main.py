
class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville._Ville__habitants += 1

ville_paris = Ville("Paris", 1000000)
print("Nombre d'habitants de la ville de Paris :", ville_paris._Ville__habitants)

ville_marseille = Ville("Marseille", 861635)
print("Nombre d'habitants de la ville de Marseille :", ville_marseille._Ville__habitants)

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print("Nombre d'habitants de la ville de Paris après l'arrivée de nouvelles personnes :", ville_paris._Ville__habitants)
print("Nombre d'habitants de la ville de Marseille après l'arrivée de nouvelles personnes :", ville_marseille._Ville__habitants)
