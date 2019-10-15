# Created function to perform IF function when called upon
def whats_there():
    print("What lies before us?")
    what_is_there = input()
    # If and else function to check whether the answer contains "a large boulder"
    if (what_is_there == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine")
# Calls on function
whats_there()