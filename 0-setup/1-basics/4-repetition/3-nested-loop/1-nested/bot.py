print("How many rows should I have?")
rows = int(input())
print("How many Columns should I have?")
Columns = int(input())
print("\nHere I go:")

for count in range(0,rows,1):
    for smileyface in range(0, Columns, 1):
        print(smileyface * ":-) ", end="")
    print()