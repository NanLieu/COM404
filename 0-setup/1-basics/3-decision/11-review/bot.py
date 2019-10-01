print("Do you want to go outside?")
response = input()
if(response == "yes"):
    print("Are you hungry?")
    hungry = input()
    if (hungry == "yes"):
        print("Let's go for Pizza!")
    else:
        print("let's go bowling!")
elif(response == "maybe"):
    print("Do you want to go to a cinema?")
    cinema = input()
    print("Do you want to watch a movie?")
    movie = input()
    if((movie == "yes") and (cinema == "yes")):
        print("Let's go to the Cinema!")
    elif((movie == "yes") and (cinema == "no")):
        print("Let's watch a movie at home!")
    elif((movie == "no") and (cinema == "yes")):
        print("What would we do at a cinema if we don't watch a film?!?!")
    else:
        print("OK, I am going home, bye!")
else:
    print("OK, bye!")
