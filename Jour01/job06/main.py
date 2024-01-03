
class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age = +1 
        ''' Augmenter l'age de l'animal de 1'''

    def nommer(self, nom):
        self.prenom = nom
        

#Instancier un objet 
animal = Animal()

#Afficher l'age de l'animal
print(animal.age)

#Vieillissement de l’animal
animal.vieillir()

#Afficher le nouveau age de l'animal
print(animal.age)

#Nommer de l'animal
animal.nommer("Jenna")

#Afficher le nom de l'animal
print("Le nom del l'animal est", animal.prenom)