# The heapqueue.py file should have a program that finds the three largest integers from a given list of numbers using Heap queue algorithm
# Expected Output:

# Original list:
numberList= [25, 35, 22, 85, 14, 65, 75, 22, 58]

# Three largest numbers are: [85, 75, 65]



def find3Largest(originalList):
    newList = originalList;
    while len(newList) >3:
        print(newList)
        def findLargest(mylist): 
            greatest = mylist[0];
            for num in mylist :
                if num <= greatest:
                    mylist.remove(num) 
                else:
                    greatest = num      
            return greatest
        findLargest(newList)
    return newList;

print(find3Largest(numberList), "function return")





