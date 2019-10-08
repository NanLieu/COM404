print("How many numbers should I sum up?")
numbers_to_sum = int(input())
number = 0
total = 0
print()

while (numbers_to_sum > number):
    number = number + 1
    print("Please enter number", number, "of ", numbers_to_sum, ":")
    input_numbers = int(input())
    total = input_numbers + total

print("\nThe answer is",total,".")

