# In your Week 2 folder, create a folder called ‘linked’ for this assignment.
# Create a linked.py file
# The linked.py file should be able to create a singly linked list, append some items and iterate through the list.


class Node:
    # should be able to create a singly linked list
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
# and iterate through the list.
    def iterate_item(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
# append some items
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

# OUTPUT GENERATED AT tuple.py