# The functions.py file should have program with Python functions that accepts a string and calculate the number of upper case letters and lower case letters.


def countingCases (string): 
    # print(string)
    # print(list(string))
    uppercases = 0
    lowercases = 0
    for x in list(string):
        if x.isupper():
            uppercases += 1
        elif x.islower():
            lowercases += 1
    print("UpperCase Count: ", uppercases)
    print("LowerCase Count: ", lowercases)
    

countingCases("Once Upon a Time in Somewhere in May")