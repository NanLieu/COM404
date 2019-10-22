# Created a function which calls specific response dependent on the parameter provided
def visit(ghost):
    # If function to determine which response is given
    if (ghost == "Ghost of Christmas Past"):
        print("Humbug! I care not for these days of past celebration.")
    elif (ghost == "Ghost of Christmas Present"):
        print("Humbug! I care not for their suffering.")
    elif (ghost == "Ghost of Christmas Future"):
        print("Please no more. I will change my ways.")
# Calls 'visit' function 3 times with 3 different parameters
visit("Ghost of Christmas Past")
visit("Ghost of Christmas Present")
visit("Ghost of Christmas Future")