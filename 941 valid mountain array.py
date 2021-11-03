# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:36:50 2021

@author: virustous
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # no left side, false
        if arr[0] >= arr[1]:
            return False
        
        # find 1st peak
        i = 0
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                i += 1
            elif arr[i] == arr[i+1]:
                return False
            else:
                break
        
        # ascending arr, false
        if i == len(arr) - 1:
            return False
        
        # check if i is the only peak (valid mountain)
        for k in range(i, len(arr)-1):
            if arr[k] <= arr[k+1]:
                return False
        return True
    
# 2nd solution, beat 95%
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''2 ppl climb from left and right separately
        if it is a valid mountain
        they will meet at the same point
        '''
        left, right, n = 0, len(arr)-1, len(arr)
        while left < n-1:
            if arr[left] >= arr[left+1]:
                break
            left += 1
        while right > 1:
            if arr[right] >= arr[right-1]:
                break
            right -= 1
        return left > 0 and left==right and right < n-1
        