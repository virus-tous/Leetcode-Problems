# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:06:29 2021

@author: virustous
"""

'''
input: array of integers - nums
        target
output: indices of 2 # that add up to target
assume each input has EXACTLY 1 sol

eg:
    input: nums = [2, 7, 11, 15], target = 9
    output: [0, 1]
    cuz nums[0] + nums[1] = 2 + 7 == 9
'''

def bruteForce(nums, target):
    '''brute force approach O(n^2)
    traverse all possible pairs
    '''
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
            
'''
2nd approach: using a hash table {n->index}
maintain a hash table for each item 'n' in 'nums', using 
'n' as key and its index as value

for each 'n', search for 'target - n'
    if it is found, return indices of 'target-n' and 'n'
    else, add 'n' to hash table and cont to find next number
    
O(n)
'''
def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return d[m], i
        else:
            d[n] = i