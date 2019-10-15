def escape_by():
    print("Boulder incoming! What's the plan?")
    plan = input()
    if (plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
        escape_by()
    elif (plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
        escape_by()
    elif (plan =="going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("We need an idea!")
        escape_by()
escape_by()

