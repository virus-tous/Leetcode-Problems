# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:18:16 2021

@author: virustous
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode
        while True:
            # if any of the lists gets empty
            # directly join all the items of the other list
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            
            # compare the data of the lists and whichever is
            # smaller is appended to resulting merged list
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # advance the tail
            tail = tail.next
        
        # return the head of the merged list
        return dummyNode.next
            
        