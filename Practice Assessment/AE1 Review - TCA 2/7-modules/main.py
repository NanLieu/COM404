
print("Please enter a word")
word = input()
from functions import *
print("Please type in an option from the following: Under, Over, Both, Grid")
option = input()
if (option == "Under"):
    print()
    under(word)
elif (option == "Over"):
    print()
    over(word)
elif (option == "Both"):
    print()
    both(word)
elif (option == "Grid"):
    print()
    grid(word)