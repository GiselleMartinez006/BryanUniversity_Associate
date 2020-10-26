# Getting Started:

# In your Week 5 folder, create a folder called ‘counting sort’ for this assignment.
# Create a countsort.py file
# The countsort.py file should have Program for counting sort.
# In the countsort.py file, write a code that displays the following output.
# Sample Output:

# [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 7]

def countsort(arr): 
    maxelement = int(max(arr)) 
    minelement = int(min(arr)) 
    range_of_elements = maxelement - minelement + 1
    # Create a count array to store count of individual 
    # elements and initialize count array as 0 
    countArr = [0 for _ in range(range_of_elements)] 
    outputArr = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
        countArr[arr[i]-minelement] += 1
  
    # Change countArr[i] so that countArr[i] now contains actual 
    # position of this element in output Array 
    for i in range(1, len(countArr)): 
        countArr[i] += countArr[i-1] 
  
    # Build the output character Array 
    for i in range(len(arr)-1, -1, -1): 
        outputArr[countArr[arr[i] - minelement] - 1] = arr[i] 
        countArr[arr[i] - minelement] -= 1
  
    # Copy the output Array to Arr, so that Arr now 
    # contains sorted characters 
    for i in range(0, len(arr)): 
        arr[i] = outputArr[i] 
  
    return arr 
  
  
# Driver program to test above function 
arr = [5, 10, 0, 3, 8, 5, 1, 10] 
ans = countsort(arr) 
print("Sorted character Array is " + str(ans)) 