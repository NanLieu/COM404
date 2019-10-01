#Ask user to enter first number
print("Please enter the first number.")
first_number = int(input())
#Ask user to enter second number
print("Please enter the second number.")
second_number = int(input())

#If statement to see which number is the smallest
if (first_number < second_number):
    print("The first number is the smallest!")
elif (first_number > second_number):
    print("The second number is the smallest!")
else:
    print("Both are equal!")