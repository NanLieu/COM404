# Ask user to input a sequence
print("Please enter a sequence")
sequence_input = input()
# Ask user to input a character for the marker
print("Please enter the character for the marker")
marker_character = input()
result = 0
# Loop command
for count in range(0, len(sequence_input) , 1):
    for dash in sequence_input:
        result = result + 1





# Provides user the answer for the distance between markers
print("The distance between the marker is", result)