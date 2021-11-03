# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:57:21 2021

@author: virustous
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # traverse the arr r2l
        rightMax = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, temp)
        arr[-1] = -1
        return arr
        