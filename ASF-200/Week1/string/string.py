# Step 3: Manipulate string
# In your Week 1 folder, create a folder called ‘string.’
# Create a string.py file
# The string.py file should ask a user their “name” and “age”
# In the input.py file, write a code that Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name? ")
yearsBeforeHundred = 100 - int(input("What is your age? "))
msg = name + " " + \
    "will turn 100 years old after " + \
    str(yearsBeforeHundred) + \
    " years; unless he/she dies before the year " + \
    str(2020 + yearsBeforeHundred) + "."
print(msg)
