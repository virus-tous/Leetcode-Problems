# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:56:18 2021

@author: virustous
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        # find frequencices of characters in s
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        # sort dict by value in descending order
        sortedChars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        
        # return the resulting string
        return ''.join([k*v for k, v in sortedChars.items()])