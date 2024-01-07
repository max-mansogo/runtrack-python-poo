
class Forme:
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14 * self.radius**2

class Rectangle(Forme):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def aire(self):
        return self.length * self.width


rectangle = Rectangle(5, 10)

aire_rectangle = rectangle.aire()
print("L'aire du rectangle est :", aire_rectangle)

cercle = Cercle(5)

aire_cercle = cercle.aire()
print("L'aire du cercle est :", aire_cercle)
