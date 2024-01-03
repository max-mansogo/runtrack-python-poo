class Operation:
    def __init__(self, num1=12, num2=3):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        résultat = self.num1 + self.num2
        print(f"Le résultat de l'addition es {résultat}")

#Instanciation de la classe
operation = Operation()

#Appele de la méthode add
operation.add()