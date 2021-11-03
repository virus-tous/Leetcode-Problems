# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:03:22 2021

@author: virustous
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # convert linked lists into numbers to add
        cur1 = l1
        cur2 = l2
        s1 = s2 = ''
        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next
        
        # read result back to a new linked list
        s3 = str(int(s1[::-1]) + int(s2[::-1]))
        head = ListNode(int(s3[0]))
        for c in s3[1:]:
            temp = ListNode(int(c))
            temp.next = head
            head = temp
        return head
            
            
            
        