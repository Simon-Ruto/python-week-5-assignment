#Class superhero with attributes and methods/behaviours
class superhero:
    def __init__(self, name, height,suit,power):
        self.name=name
        self.height=height
        self.suit=suit
        self.power=power

    def save(self,saved):
        print(f"{self.name} who's {self.height} with a {self.suit} suit saved {saved}, with his {self.power} superpower.")   

    def beat(self,villian):
        print(f"{self.name} with his {self.power} beat the {villian}")  

#Inheritance from the class superhero to minihero with an example of encapsulation
class minihero(superhero):
    def __init__(self, name, height, suit, power,age):
        super().__init__(name, height, suit, power)
        self.__age=age

    def does(self,activity):
        print(f"The mini hero {self.name} who is {self.height}, {self.__age} years and with a normal {self.suit} {activity} people due to his {self.power}.")   

         

super_hero1=superhero("John","6.2","black","speed")
super_hero1.save("a child")   

normal_hero=minihero("Jude","5.5","attire","kindness","24")
normal_hero.does("helps")

        