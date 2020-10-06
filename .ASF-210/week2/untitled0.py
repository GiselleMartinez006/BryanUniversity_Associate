# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:06:26 2020

@author: 17865
"""

# =============================================================================
# class Node:
# 
#     def __init__(self, data):
#     
#         self.left = None
#         self.right = None
#         self.data = data
#     
#     # Insert method to create nodes
#     def insert(self, data):
#     
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                     if self.right is None:
#                         self.right = Node(data)
#             else:
#                 self.right.insert(data)
#         else:
#             self.data = data
#     # findval method to compare the value with nodes
#     def findval(self, lkpval):
#         if lkpval < self.data:
#             if self.left is None:
#                 return str(lkpval)+" Not Found"
#                 return self.left.findval(lkpval)
#             elif lkpval > self.data:
#                 if self.right is None:
#                     return str(lkpval)+" Not Found"
#                     return self.right.findval(lkpval)
#                 else:
#                     print(str(self.data) + ' is found')
#     # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
# 
# 
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# print(root.findval(7))
# print(root.findval(14))


array = [1,5,2,7,-2,12,11,8,9,-6,4]

for a in range(len(array)):
    print(a, "aaaaaaaaaaaaaaaaaaaaaa")
    for b in range(a, len(array)):
        c = sum(array[a:b+1])
        print("C",c)
        print(b, "bbbbb")
    
# =============================================================================
# def three_loops(array):
#     print("array",array)
#     n = len(array)
# # =============================================================================
# #     print("n",n)   => 11
# # =============================================================================
# # =============================================================================
# #     print("range(n)",range(n)) => range(0,11)
# # =============================================================================
#     max_sum=array[0]
# # =============================================================================
# #     print("max_sum",max_sum)  => starts as 1
# # =============================================================================
#     for start in range(n):
# # =============================================================================
# #         print("start",start) => here start is like each index of the array, first one being 0
# # =============================================================================
# # =============================================================================
# #         print("range(start,n)",range(start,n))  => here is listing out the numbers from start (current index) to 11 which is the end of len
# # =============================================================================
#         for end in range(start, n):
# # =============================================================================
# #             print("end",end)  => end is the INDEX from 0-11 per start number
# # =============================================================================
#             current_sum = sum(array[start:end+1])
#             
#             print("current_sum", current_sum)
#             print ("max_sum", max_sum)
#             
# # =============================================================================
# #  IF CURRENT SUM IS BIGGER THAN THE BIGGEST RECORDED SO FAR
# # then THE BIGGEST RECORDED SO FAR WILL BE CURRENT SUM
# # =============================================================================
# 
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 
#     print ("82 max_sum", max_sum)            
#     return max_sum
# 
# three_loops(array)
# # =============================================================================
# =============================================================================
