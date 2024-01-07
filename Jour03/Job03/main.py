
class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(f"Titre : {tache.titre}")
            print(f"Description : {tache.description}")
            print(f"Statut : {tache.statut}")
            print("")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

'''Création des tâches et liste de tâches'''
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Appeler le médecin", "Prendre rendez-vous pour le check-up annuel")
tache3 = Tache("Faire du sport", "Aller à la salle de sport et faire une séance d'entraînement")

listeDeTaches = ListeDeTaches()

listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

print("Liste de toutes les tâches :")
listeDeTaches.afficherListe()

'''Marquer une tâche terminée'''
listeDeTaches.marquerCommeFinie(tache2)

'''liste de tâches après avoir marqué une tâche comme terminée'''
print("Liste de toutes les tâches après avoir marqué une tâche comme terminée :")
listeDeTaches.afficherListe()

'''Tâches par statut'''
taches_a_faire = listeDeTaches.filterListe("à faire")
print("Liste des tâches à faire :")
for tache in taches_a_faire:
    print(f"Titre : {tache.titre}")
    print(f"Description : {tache.description}")
    print("")

'''Supprimer une tâche de la liste'''
listeDeTaches.supprimerTache(tache3)

'''Liste de tâches après avoir supprimé une tâche'''
print("Liste de toutes les tâches après avoir supprimé une tâche :")
listeDeTaches.afficherListe()
