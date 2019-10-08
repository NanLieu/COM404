# Ask user question
print("How many live cables should I avoid?")
# User input of live cables to avoid
avoid_cables = int(input())
# Counter of live cables avoided
live_cables = 0
while (live_cables < avoid_cables):
    live_cables = live_cables + 1
    print("Avoiding...Done!", live_cables, "live cables avoided.")
print("All live cables have been avoided.")