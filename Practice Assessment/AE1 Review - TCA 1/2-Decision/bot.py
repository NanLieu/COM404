# Presents user with a question
print("Where is Forky?")
# Requests user's input for Forky's wherabouts
where_forky = input()
# Decision: 3 responses dependent on what the user has inputted
if (where_forky == "With Bonnie"):
    print("Phew! Bonnie will be happy")
elif (where_forky == "Running away"):
    print("Oh no! Bonnie will be upset!")
# Last response if none of the input matches the above
else:
    print("Ah! I better look for him")