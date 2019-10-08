print("What phrase do you see?")
phrase = input()
# Setting result up as a string variable
result = ""
print("Reversing...")
#  for (variable) in (variable)
# do variable1 = variable2 + variable1

for letter in phrase:
    result = letter + result

print("The phrase is:",result)
