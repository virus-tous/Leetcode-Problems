# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:10:13 2021

@author: virustous
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n==0:
            return 1
        if n%2 == 0:
            return self.myPow(x*x, n//2)
        if n%2 == 1:
            return x * self.myPow(x*x, (n-1)//2)
        