from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, hover_distance=100):
        super().__init__(name, age)
        self.hover_distance = hover_distance

    def get_hover_distance(self):
        return self.hover_distance

    def set_hover_distance(self, hover_distance):
        self.hover_distance = hover_distance


