
class Livre:
    def __init__(self, titre, auteur, num_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__num_pages = num_pages
        self.__disponible = True

    #Getters et Setters
    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_num_pages(self):
        return self.__num_pages

    def set_num_pages(self, num_pages):
        if isinstance(num_pages, int) and num_pages > 0:
            self.__num_pages = num_pages
            '''nombre de pages positif'''
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")

    def get_disponible(self):
        return self.__disponible
    
     #Vérifier si le livre est disponible
    def vérification(self):
        return self.__disponible

    #Emprunter le livre
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    #Rendre le livre
    def rendre(self):
        if not self.vérification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté, donc ne peut pas être rendu.")

# Creer un objet Livre
livre = Livre("El Gran Gatsby", "F. Scott Fitzgerald", 300)

# Afficher le titre
print(livre.get_titre())  # Output: El Gran Gatsby

# Modifier le nombre de l'auteur du livre
livre.set_auteur("Jane Austen")

# Afficher le nouveau auteur du livre
print(livre.get_auteur())  # Output: Jane Austen

# Modifier le nombre de pages du livre
livre.set_num_pages(400)

# Afficher le nouveau nombre de pages du livre
print(livre.get_num_pages())  # Output: 400

#Vérifier la disponibilité du livre
print("Le livre est disponible :", livre.vérification())

#Emprunter le livre
livre.emprunter()

#Vérifier à nouveau la disponibilité du livre
print("Le livre est disponible :", livre.vérification())

#Rendre le livre
livre.rendre()

#Vérifier à nouveau la disponibilité du livre
print("Le livre est disponible :", livre.vérification())
