def display_ladder(steps):
    for count in range(0, steps, 1):
        print("| |")
        print("***")
    print("| |")



def create_ladder():
    steps = int(input())
    display_ladder(steps)


print("how many steps remain?")
create_ladder()
