
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"
    '''On pourrait aussi mettre le prénom en première place'''
    
#Instanciation des personnes
personne1 = Personne("DOE", "John")
personne2 = Personne("DUPOND", "Jean")
personne3 = Personne("MANSOGO", "Max")

#Appeler la méthode SePrenter
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())