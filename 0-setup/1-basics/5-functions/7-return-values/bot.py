# Function for the sum of the robot's weight, returns value of total weight
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

# Function for the average of the robot's weight, returns value of average weight
def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight)/2
    return avg_weight

# Main function which records user's input and has if function to decide which which other function to run calculations
def run():
    print("What is the weight of Beep?")
    beep_weight = int(input())
    print()
    print("What is the weight of Bop?")
    bop_weight = int(input())
    print()
    print("What would you like to calculate (sum or average)?")
    response = input()
    if (response == "sum"):
        print("\nThe sum of Beep and Bop's weight is", sum_weights(beep_weight, bop_weight))
    elif (response == "average"):
        print("\nThe average of Beep and Bop's weight is", calc_avg_weight(beep_weight, bop_weight))


run()