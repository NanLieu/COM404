# Creates function with 1 parameter
def cross_bridge(steps):
    # Loop to count how many steps taken and prints a message dependent on how many steps taken
    for step in range(0, steps, 1):
        print("Crossed step.")
    if (steps < 5):
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")

# Calls function twice with 2 different parameter
cross_bridge(3)
cross_bridge(6)