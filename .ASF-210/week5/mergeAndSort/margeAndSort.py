# In your Week 5 folder, create a folder called ‘merge sort’ for this assignment.
# Create a mergesort.py file
# The mergesort.py file should be able to sort a list of elements using the merge sort algorithm.
# In the mergesort.py file, write a code that displays the following output.
# Sample Output:

# Splitting  [14, 46, 43, 27, 57, 41, 45, 21, 70]                                                               

# Splitting  [14, 46, 43, 27]                                                                                  

# Splitting  [14, 46]                                                                                           

# Splitting  [14]                                                                                              

# Merging  [14]                                                                                                

# Splitting  [46]                     

# -------

# Merging  [14, 21, 27, 41, 43, 45, 46, 57, 70]                                                                

# [14, 21, 27, 41, 43, 45, 46, 57, 70]

array = [14, 46, 43, 27, 57, 41, 45, 21, 70]  

def mergeSortAlgorithm(array):
    def merge(arr, l, m, r): 
        n1 = m - l + 1
        n2 = r- m 

        # create temp arrays 
        L = [0] * (n1) 
        R = [0] * (n2) 

        # Copy data to temp arrays L[] and R[] 
        for i in range(0 , n1): 
            L[i] = arr[l + i] 

        for j in range(0 , n2): 
            R[j] = arr[m + 1 + j] 

        # Merge the temp arrays back into arr[l..r] 
        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = l     # Initial index of merged subarray 

        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there 
        # are any 
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there 
        # are any 
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1

    # l is for left index and r is right index of the 
    # sub-array of arr to be sorted 
    def mergeSort(arr,l,r): 
        if l < r: 
    
            # Same as (l+r)//2, but avoids overflow for 
            # large l and h 
            m = (l+(r-1))//2
    
            # Sort first and second halves 
            mergeSort(arr, l, m) 
            mergeSort(arr, m+1, r) 
            merge(arr, l, m, r) 
    
    
    # Driver code to test above 
    arr = [1,3, 2,2,3,1,4,2,7,1,2] 
    
    n = len(arr) 
    
    mergeSort(arr,0,n-1) 
    print ("arr", arr) 
    
  


mergeSortAlgorithm(array)
