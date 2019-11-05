class Bot:



    # Constructor
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    # Methods
    def display_name(self):
        #print("----------")
        #print("|   {}   |".format(self.name))
        #print("----------")
        print("*" * (len(self.name) + 4))
        print("*", self.name, "*")
        print("*" * (len(self.name) + 4))

    def display_age(self):
        print("  ", self.age,"  ")
        print("  ----  ")
        print(" |    |")
        print(" ------")

    def display_energy(self):
        print("█ " * self.energy)

    def display_shield(self):
        print("Σ " * self.shield)

    def display_summary(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Energy: {}".format(self.energy))
        print("Shield: {}".format(self.shield))

    def __str__(self):
        return "My name is {}".format(self.name)

bot1 = Bot("Alex", 40, 8, 10)
print()
#bot1.display_name()
#bot1.display_age()
#bot1.display_energy()
#bot1.display_shield()
#print()
bot1.display_summary()
print()
#print(bot1.__str__())
