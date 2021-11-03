# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:12:55 2021

@author: virustous
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 1
        end = x//2 + 1
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans
                
        