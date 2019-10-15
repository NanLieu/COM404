# Defined a function with the parameter "plan" with if function built in
def escape_by(plan):
    if (plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif (plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (plan =="going deeper"):
        print("That might just work! Let's go deeper!")

# Calls function with a defined parameter
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
