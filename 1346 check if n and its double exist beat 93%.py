# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:14:10 2021

@author: virustous
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = []
        for i in range(len(arr)):
            if 2*arr[i] in l:
                return True
            elif arr[i]%2 == 0:
                if arr[i] // 2 in l:
                    return True
            l.append(arr[i])
        return False