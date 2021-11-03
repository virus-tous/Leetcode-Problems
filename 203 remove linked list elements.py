# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:22:57 2021

@author: virustous
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
            
        if head is None:
            return head
        else:
            predNode = head
            curNode = head.next
            if predNode is not None:
                while curNode is not None:
                    if curNode.val == val:
                        predNode.next = curNode.next
                        curNode = curNode.next
                    else:
                        predNode = curNode
                        curNode = curNode.next
        return head
        