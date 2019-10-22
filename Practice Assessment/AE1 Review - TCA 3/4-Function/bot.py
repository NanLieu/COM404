def spideysense (enemy, direction):
    if (enemy == "Green Goblin"):
        print("Goblin bombs incoming from " + direction)
    elif (enemy == "Venom"):
        print("Venomous webbing incoming from " + direction)
    elif (enemy == "Electro"):
        print("Electro striking from " + direction)
    else:
        print("New enemy attacking from "+ direction),

spideysense("Green Goblin", "front")
spideysense("Venom", "behind")
spideysense("Electro", "left side")
spideysense("Unknown", "right side")