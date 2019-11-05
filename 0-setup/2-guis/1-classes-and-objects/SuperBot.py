from bot import Bot

class SuperBot(Bot):
    def __init__(self, name, age, power_level):
        super().__init__(name, age)
        self.power_level = power_level

    def get_power_level(self):
        return self.power_level

    def set_power_level(self, power_level):
        self.power_level = power_level



