from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, energy, shield, power_level, hover):
        super().__init__(name, age, energy, shield, power_level)
        self.hover = hover

    def display_hover_level(self):
        print(self.hover)

bot3 = FlyingBot("Kal El", 20, 10, 10, 100, 50)
bot3.display_hover_level()
bot3.display_summary()
