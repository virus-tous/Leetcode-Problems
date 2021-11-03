# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:15:05 2021

@author: virustous
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(list(s))) == ''.join(sorted(list(t)))
        