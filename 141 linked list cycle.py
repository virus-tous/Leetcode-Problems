# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:12:44 2021

@author: virustous
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Floyd's Cycle-Finding Alg
        slow_p = fast_p = head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # traverse all nodes, if a node is met again -> there exists a circle
        if head == None or head.next == None:
            return False
        nodes = []
        cur = head
        while cur.next:
            if cur.next in nodes:
                return True
            nodes.append(cur)
            cur = cur.next
        return False