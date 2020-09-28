# The List.py file should be able to insert items into a list in sorted order
# In the input.py file, write a code that displays following output.
# Expected Output:

# Original List:

originalList = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

# Sorted List:

# [14, 25, 36, 36, 45, 47, 48, 68, 69, 78] 

originalList.sort()  #getting the original list in sorted order
newList = []

for num in originalList: 
    newList.append(num) #inserting nums in the new list after they've been sorted

print(newList)