# Ask user to input a sequence
print("Please enter a sequence")
sequence = input()
# Ask user to input a character for the marker
print("Please enter the character for the marker")
marker = input()

# Find markers, positioned outside of the range calculations so it doesn't get counted
marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1_position == -1):
            marker1_position = position
        else:
                marker2_position = position

# Display result
print("The distance between the markers is", marker2_position - marker1_position - 1)