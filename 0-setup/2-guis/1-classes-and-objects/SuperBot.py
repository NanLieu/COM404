from bot import Bot

class SuperBot(Bot):
    def __init__(self, name, age, energy, shield, power_level):
        super().__init__(name, age, energy, shield)
        self.power_level = power_level

    def display_power_level(self):
        print("Super Bot", self.name)
        print("Power Level:", self.power_level)
        print()

bot2 = SuperBot("Dave", 25, 10, 10, 10)
bot2.display_power_level()