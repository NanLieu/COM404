print("Where should I look?")
where_to_look = input()
if (where_to_look == "in the bedroom"):
    print("Where in the bedroom should I look?")
    in_bedroom = input()
    if (in_bedroom == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
elif (where_to_look == "in the bathroom"):
    print("Where in the bathroom should I look?")
    in_bathroom = input()
    if (in_bathroom == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery")
elif (where_to_look == "in the lab"):
    print("Where in the lab should I look?")
    in_lab = input()
    if (in_lab == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking.")

print("hurrah!")

