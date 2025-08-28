# Polymorphism Challenge  (Superheroes)

class Superhero:
    def action(self):
        raise NotImplementedError("Subclass must implement this method")

class Superman(Superhero):
    def action(self):
        print(" Superman is flying high in the sky!")

class Batman(Superhero):
    def action(self):
        print(" Batman is driving the Batmobile through Gotham!")

class Flash(Superhero):
    def action(self):
        print("Flash is running at super speed!")

class WonderWoman(Superhero):
    def action(self):
        print("Wonder Woman is blocking with her shield!")

class SpiderMan(Superhero):
    def action(self):
        print("Spider-Man is swinging between buildings!")

# List of superheroes
heroes = [Superman(), Batman(), Flash(), WonderWoman(), SpiderMan()]

# Demonstrate polymorphism
for hero in heroes:
    hero.action()
