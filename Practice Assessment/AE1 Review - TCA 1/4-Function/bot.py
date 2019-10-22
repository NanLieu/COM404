# Created function to determine what code to run dependent on the parameter
def item_from_suitcase (item):
    if (item == "toothbrush"):
        print("A toothbrush. Well, got to have clean teeth!\n")
    elif (item == "spidey suit"):
        print("My Spidey suit! I won't be needing this. I am on holiday.\n")
    else:
        print("An unexpected item! It could be useful.\n")
# Prints first statement for user
print("I wonder what is in my suitcase...\n")
# Calls function 3 times with 3 different parameters
item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")