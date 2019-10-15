def ascii_box(word):
    print("-------------")
    print("| ", word, " |")
    print("-------------")

def lower_case(word):
    print(word.lower())

def upper_case(word):
    print(word.upper())

def display_mirrored(word):
    for position in range(len(word) - 1, -1 , -1):
        print(word[position], end="")
    print()

def repeat(word, number_of_repeats):
    for count in range(0, number_of_repeats, 1):
        if (count % 2 != 0):
            print(word.upper())
        else:
            print(word.lower())


def run():
    print("Please enter a word for alteration!")
    word = input()
    print("Please choose how you would like the word to be altered. Box, Lower, Upper, Mirrored, Repeated")
    alteration_type = input()

    if (alteration_type == "Box"):
        ascii_box(word)

    elif (alteration_type == "Lower"):
        lower_case(word)

    elif (alteration_type == "Upper"):
        upper_case(word)

    elif (alteration_type == "Mirrored"):
        display_mirrored(word)

    elif (alteration_type == "Repeated"):
        print("How many times?")
        number_of_repeats = int(input())
        repeat(word, number_of_repeats)

run()