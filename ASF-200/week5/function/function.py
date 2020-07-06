# The function.py file should have Python function to find the Max of three numbers.

def maxOfThree (a,b, c): 
    sequence=[a,b,c]
    sequence.sort()     
    # printing the last element 
    print("The biggest number is: ", sequence[-1]) 
    

maxOfThree(2,5,45)

