# Setting value of variable for 'health' at 100
health = 100
# Print statement stating amount of 'health' and the code is starting
print("You health is",health,"%. Escape is in progress")
# For loop which loops 5 time stated in the range
for count in range(0, 5, 1):
    print("...Oh dear, who is that?")
    # Awaits user's input to put into 'who' variable
    who = input()
    # if function to determine which code is run based on the user's input
    if (who == "Smiler's Bot"):
        # negative adjustment to 'health' value
        health = health - 20
        print("Time to jam out of here!")
    elif (who == "Hacker"):
        # positive adjustment to 'health' value
        health = health + 20
        print("Yay! Better follow this one!")
    else:
        # Prints statement if user's input doesn't matches anything
        print("Phew, just another emoji!")
# Prints final statement with remaining 'health' value
print("Escape! Health is",health,"%.")