# Ask user a question
print("How many miles must I travel before I reach the secret base?")
# Request an integer input from the user
miles_left = int(input())
# Print message of countdown beginning
print("I will count the miles...\n")
# while loop, will loop as long as 'miles_left' is higher than 0
while (miles_left > 0):
    # Prints message with the current miles left using the 'miles_left' variable
    print("I have",miles_left,"miles to go before I reach the base.")
    # 'miles_left' -1 per loop, act as a countdown
    miles_left = miles_left - 1
# New line with \n code, prints message of arriving and sneaking in
print("\nI have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")
