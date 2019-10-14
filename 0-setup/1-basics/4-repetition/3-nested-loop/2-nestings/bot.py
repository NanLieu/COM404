# Ask user to input a sequence
print("Please enter a sequence")
sequence_input = input()
# Ask user to input a character for the marker
print("Please enter the character for the marker")
marker_character = input()
answer = 0
# Loop command
for characters in sequence_input:
    for dashes in range(len(marker_character), len(marker_character), 1):
        answer = answer + 1
# Provides user the answer for the distance between markers
print("The distance between the marker is", answer)