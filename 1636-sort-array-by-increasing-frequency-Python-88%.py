# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:44:07 2021

@author: virustous
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
                
        return sorted(nums, key=lambda  x: (freq[x], -x))
        
        