#  For this one the array was the same as binarysearch assignment
#  and my balaced tree for that one is already a height balanced Binary Search Tree
# So ... for this one just added a function that verifies that it is so!

# my_array = [1,2,3,4,5,6,7]
my_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


def balance(arr):
    new_arr =[]
    new_arr += arr;
    treeOrder =[]

    def findingRoot(array):
        finding0Root = array[(len(array)//2)]
        # print(finding0Root)
        treeOrder.append(finding0Root)
        array.remove(finding0Root)
        
    findingRoot(new_arr)

    rootindex = (len(new_arr)//2)
    # print(treeOrder)
    
    left = new_arr[0:rootindex]
    # print(new_arr[0:rootindex])
    while len(left) > 2:
        findingRoot(left)
        # print(left)
        

        # for num in len(left):
        #     left.remove(num)
    treeOrder += left
    right = new_arr[rootindex:]
    # print(new_arr[rootindex:])

    while len(right) > 2:
        findingRoot(right)
        # print(right)
        

        # for num in len(right):
        #     right.remove(num)
    treeOrder += right
    return treeOrder

    

my_bst = balance(my_array)
print ("my_bst",my_bst)


def isHeight(originalArray, balancedArray):
    print(originalArray)
    findingOriginalRoot = originalArray[(len(originalArray)//2)]
    
    findingBSTroot = balancedArray[0]

    if findingBSTroot != findingOriginalRoot:
        print(findingBSTroot, findingOriginalRoot)
        print("""if these two are not the same it is already wrong 
        because the root is the point where left and right are broken at. 
        Hence if they are not the same that means that the BST got a root 
        other than exactly the one in the middle.""")
    else:
        # if the roots are both the same and right. we can get them out of the way for now.
        balancedArray.remove(findingBSTroot)
        originalArray.remove(findingOriginalRoot)
        
        # Let's find the right and lefts of each

        originalLeft = originalArray[0:(len(originalArray)//2)]
        originalRight =originalArray[(len(originalArray)//2):]

        lengthLeft = len(originalLeft)
        lengthRight= len(originalRight)

        balancedLeft = balancedArray[0:(len(originalArray)//2)]
        balancedRight =balancedArray[(len(originalArray)//2):]

        lengthBSTLeft = len(balancedLeft)
        lengthBSTRight= len(balancedRight)

        if lengthBSTLeft != lengthLeft:
            print("if both lefts don't have the same length is wrong already")
        if lengthBSTRight != lengthRight:
            print("if both rights don't have the same length is wrong already")

        print("originalLeft", originalLeft)
        print("balancedLeft", balancedLeft)
        print("originalRight", originalRight)
        print("balancedRight", balancedRight)
        
        print ("last but not least, comparing the heights of the left and right")
        if len(balancedLeft) != len(balancedRight):
            if len(balancedLeft) < len(balancedRight):
                if len(balancedRight) - len(balancedLeft) > 1:
                    print("Not height balanced!")
            if len(balancedLeft) > len(balancedRight):
                if len(balancedLeft) - len(balancedRight) > 1: 
                    print("Not height balanced!")

        print("it is height balanced")
  

isHeight(my_array, my_bst)
      
    # left = arr[0:rootindex]
    # right = arr[rootindex:]


