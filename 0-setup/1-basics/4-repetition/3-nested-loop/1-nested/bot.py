# Ask question about rows
print("How many rows should I have?")
# User response for rows question
rows = int(input())
# Ask quest about columns
print("How many Columns should I have?")
# User response for column questsion
Columns = int(input())
# Initialising message for user
print("\nHere I go:")
# Loop which checks how many times to run the command per row
for count in range(0,rows,1):
    # Loop to print the number of smileyfaces per column
    for smileyface in range(0, Columns, 1):
        print(smileyface * ":-) ", end="")
    print()