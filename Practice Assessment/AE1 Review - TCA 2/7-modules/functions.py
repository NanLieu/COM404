def under(word):
    print(word)
    print("*****")

def over(word):
    print("*****")
    print(word)

def both(word):
    print("*****")
    print(word)
    print("*****")

def grid(word):
    print("What size grid?")
    size_of_grid = int(input())

    for count in range(0, size_of_grid, 1):
        print("***** " * size_of_grid)
        print((word + " | ")  * size_of_grid)
        print("***** " * size_of_grid)
        print()
