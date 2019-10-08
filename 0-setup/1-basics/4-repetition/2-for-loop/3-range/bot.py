print("What level of brightness is required?")
brightness = int(input())
print("Adjusting brightness...")
for count in range(2, brightness+1, 2):
    print("Beep's brightness level:", count * "*")
    print("Bop's brightness level:", count * "*")
print("\nAdjustments complete!")