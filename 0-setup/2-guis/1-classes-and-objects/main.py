from bot import Bot
from SuperBot import SuperBot
from FlyingBot import FlyingBot

bot1 = Bot("Charlie", 10, 100, 100)
bot2 = SuperBot("Dave", 50, 100)
bot3 = FlyingBot("Bob", 30)

bot1.display_summary()
bot2.display_age()
bot3.get_hover_distance()





