# Ask user what they heard
print("What did I hear?")
hear = input()
# Ask user what they saw
print("What did I see?")
see = input()

# Identify and determine action
if((hear == "grr") and (see == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")