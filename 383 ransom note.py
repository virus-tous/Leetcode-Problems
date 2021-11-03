# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:57:28 2021

@author: virustous
"""

# hash table
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for c1 in ransomNote:
            if c1 in d1:
                d1[c1] += 1
            else:
                d1[c1] = 1
        for c2 in magazine:
            if c2 in d2:
                d2[c2] += 1
            else:
                d2[c2] = 1
                
        for k in d1:
            if (k not in d2) or (d1[k] > d2[k]):
                return False
        return True
    
# create a list of frequencies of characters
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars1 = [0] * 26
        chars2 = [0] * 26
        for c in ransomNote:
            chars1[ord(c) - ord('a')] += 1
        for c in magazine:
            chars2[ord(c) - ord('a')] += 1
        for i in range(len(chars1)):
            if chars1[i] > chars2[i]:
                return False
        return True
        