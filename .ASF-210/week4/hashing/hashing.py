# The hashing.py file should be able to print the integer hash value, string has value and float hash value..
# In the tuple.py file, write a code that displays following output.
# Expected Output:

# The output for the above program will be: 
    #you shouldprobably tell us what to hash and to test the output of that
    # but nonetheless, I found it here: https://www.edureka.co/blog/hash-in-python/
int_val = 4
str_val = 'PythonIsBest'
flt_val = 24.56


# The integer hash value is:4    
print(hash(4))                                                                                                        
# The string hash value is: 2063534490514258345
print(hash(str_val))  #basically gets a new different hash every time i run it!   
# The float hash value is:1291272085159665688
print(hash(flt_val))  


# print(hash("4"))
# print(hash(4.5))



# =============================================================================
# =============================================================================
# import basehash# 
# hash_fn = basehash.base36()  # you can initialize a 36, 52, 56, 58, 62 and 94 base fn
# =============================================================================
# hash_value = hash_fn.hash(4.5) # returns 'M8YZRZ'
# unhashed = hash_fn.unhash(hash_value) # returns 1
# =============================================================================

