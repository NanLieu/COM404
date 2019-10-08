# Question
print("What phrase do you see?")
# User Input
phrase = input()
# Displaying message
print("\nReversing...\n")
# Display message whilst intending to add extra test at the end
print("\nThe phrase is: ", end="")
#For loop of position in phrase variable,
for position in range(len(phrase) - 1, -1 , -1):
    # print phrase based on position
    print(phrase[position], end="")
print()



