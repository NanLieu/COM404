# Function 1 with 2 parameters, 'hero1' and 'hero2'
def is_league_united(hero1, hero2):
    # if function to see if Superman or Wonder Woman are used in 'hero1' or 'hero2' and returns a True or False
    if (hero1 == "Superman" and hero2 == "Wonder Woman") or (hero1 == "Wonder Woman" and hero2 == "Superman"):
        return True
    else:
        return False

# Function 2 with 2 parameters
def decide_plan(hero1, hero2):
    # Determines if Function 1 has returned a True message and returns a message, otherwise it would return a different message
    if (is_league_united(hero1, hero2) == True):
        return "Time to save the world!"
    else:
        return "We must unite the league!"

# Function 3, contains main code to call functions
def run():
    # Asks user to enter Hero 1's name
    print("Please enter first hero's name")
    hero1 = input()
    # Asks user to enter Hero 2's name
    print("Please enter second hero's name")
    hero2 = input()
    # Asks user to input either 'League' or 'Plan'
    print("League or Plan?")
    decision = input()
    # If function to determine which function to run with the parameters that it has received and print the response
    if (decision == "League"):
        print(is_league_united(hero1, hero2))
    elif (decision == "Plan"):
        print(decide_plan(hero1, hero2))
    else:
        print("Invalid command. Please try again")

# Calls the 'run' function
run()