print("How far are we from the cave?")
distance = int(input())
print()
for count in range(distance, 0, -1):
    print(distance," steps remaining")
    distance = distance - 1
print("\nWe have reached the cave!")

