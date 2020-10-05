# In the tuple.py file, write a code that displays the following output. 
# Expected Output:

# PHP
# Python
# C#
# C++
# Java



from linked import singly_linked_list
# =============================================================================
# print (singly_linked_list)
# =============================================================================
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

#printing output
for val in items.iterate_item():
    print(val)
    
    