# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:24:48 2021

@author: virustous
"""

'''
input: arr of ints - numbers - in non-decreasing order
        target
output: indices of 2 items that add up to target (added by 1)
assume there is exactly 1 sol, may not use the same item twice




'''

# two pointers
# O(n) time
# O(1) space
def twoSum(nums, target):
    first = 0
    last = len(nums) - 1
    while first < last:
        if nums[first] + nums[last] == target:
            return first+1, last+1
        elif nums[first] + nums[last] > target:
            last -= 1
        else:
            first += 1
# end f. twoSum
            
# dictionary
# O(n) time
# O(n) space
def twoSum2(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n 
        if m in d:
            return d[m]+1, i+1
        else:
            d[n] = i
# end f. twoSum2


# 3. binary search
# O(NlogN)
# cuz binary search in a loop
def twoSum3(nums, target):
    for i in range(len(nums)):
        low, high = i+1, len(nums)-1
        # 1st operand is nums[i]
        # find 2nd operand from i+1
        m = target - nums[i]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == m:
                return i+1, mid+1
            elif nums[mid] > m:
                high -= 1
            else:
                low += 1
    
