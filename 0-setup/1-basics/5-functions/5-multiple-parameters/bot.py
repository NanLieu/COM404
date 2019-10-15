# function with 2 parameters of the number of steps taken and number of steps left
def climb_ladder(steps_taken, steps_left):
    # if function to compare the 2 parameters
    if (steps_taken < steps_left):
        print("Still some way to go!")
    else:
        print("We made it!")
# Calls the function twice with 2 set parameters
climb_ladder(2,5)
climb_ladder(5,5)