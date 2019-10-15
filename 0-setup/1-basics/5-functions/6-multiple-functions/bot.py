# function 1 : ladder creation
def display_ladder(steps):
    # Loop for creating acsii ladder
    for count in range(0, steps, 1):
        print("| |")
        print("***")
    print("| |")


# function 2 : Identifies the number of steps required from the ladder
def create_ladder():
    # User input of steps remaining
    steps = int(input())
    # Calls ladder creation function with the parameter entered by the user
    display_ladder(steps)

# Code starts here! Prompts user a question
print("how many steps remain?")
# Calls function 2
create_ladder()
