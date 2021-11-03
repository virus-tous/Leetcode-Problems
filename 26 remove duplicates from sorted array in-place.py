# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:01:40 2021

@author: virustous
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        k = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k