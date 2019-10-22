print("How many heroes must we gather>")
gather = int(input())
print("Gathering heroes...")
hero_gathered = 0
for number in range(0, gather, 1):
    hero_gathered = hero_gathered + 1
    print("...found hero",hero_gathered)
print("...all the heroes have been gathered")