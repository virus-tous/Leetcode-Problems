# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:27:42 2021

@author: virustous
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # get frequencies of each number in arr
        freq = {}
        for n in arr:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
                
        # sort the dict by value for easily detecting duplicate frequencies
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        
        curVal = 0
        for v in sorted_freq.values():
            if v == curVal:
                return False
            curVal = v
        return True
        