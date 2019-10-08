print("What strange markings do you see?")
markings = input()
print("\nIdentifying...\n")
for position in range(0, len(markings), 1):
    print("index", position, ":", markings[position])
print("\nDone!")
