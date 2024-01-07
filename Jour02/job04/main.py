
#Partie 1

'''

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0

    def add_credits(self, quantite):
        if quantite > 0:
            self.__credits += quantite
        else:
            print("Erreur : La quantité de crédits doit être supérieure à zéro.")

    def get_total_credits(self):
        return self.__credits

# Instanciation d'un objet représentant l'étudiant John Doe avec le numéro d'étudiant 145
etudiant_john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
etudiant_john_doe.add_credits(10)
etudiant_john_doe.add_credits(20)
etudiant_john_doe.add_credits(30)

# Impression du total de crédits en console
print("Total de crédits de l'étudiant John Doe :", etudiant_john_doe.get_total_credits())

'''

#Partie 2 (code modifié)

class Etudiant:
    def __init__(self, prenom, nom, numero_etudiant):
        self.__prenom = prenom
        self.__nom = nom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__niveau = self.__evaluation_etudiant()

    def ajouter_credits(self, quantite):
        if quantite > 0:
            self.__credits += quantite
            self.__niveau = self.__evaluation_etudiant()

    def __evaluation_etudiant(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Suffisant"
        else:
            return "Insuffisant"

    #Avoir le total des crédits ajoutés    
    def get_total_credits(self):
        return self.__credits

    def informations_etudiant(self):
        print("Prénom:", self.__prenom)
        print("Nom:", self.__nom)
        print("Numéro d'étudiant:", self.__numero_etudiant)
        print("Niveau:", self.__niveau)

#Créer un objet Etudiant
etudiant = Etudiant("John", "Doe", 145)

#Ajouter des crédits à l'étudiant
etudiant.ajouter_credits(20)
etudiant.ajouter_credits(30)
etudiant.ajouter_credits(25)

#Imprimer les informations de l'étudiant
etudiant.informations_etudiant()
