print("How many bars should be charged?")
bars_to_charge = int(input())
charged_bars = 0
while(charged_bars < bars_to_charge):
    charged_bars = charged_bars + 1
    print("Charging:", "█ " * charged_bars)
print("The battery is fully charged.")

