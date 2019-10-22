# Dr Bravestone asks a question
print("How many zones must I cross?")
# Awaits user response in form of a whole number
zones = int(input())
# Prints statement
print("Crossing zones...")
# Runs while loop function which will loop as long as 'zones' is greater than 0
while (zones > 0):
    # prints message with the current 'zone'
    print("...crossed zone",zones)
    # countdown for 'zones' each time it is looped
    zones = zones - 1
# Print final message when loop is complete
print("Crossed all zones. Jumanji!")