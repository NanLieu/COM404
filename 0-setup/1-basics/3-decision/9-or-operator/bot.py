print("What type of adventure do you want to go on?")
adventure_type = input()
if(adventure_type == "scary") or (adventure_type == "short"):
    print("Entering the Dark Forest!")
elif(adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")