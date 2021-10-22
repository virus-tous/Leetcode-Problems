# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:53:31 2021

@author: virustous
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        subarr = []
        output = []
        for n in nums:
            if subarr == [] or subarr[-1]+1 == n:
                subarr.append(n)
            else:
                if len(subarr) == 1:
                    output.append(str(subarr[-1]))
                else:
                    output.append(str(subarr[0]) + "->" + str(subarr[-1]))
                subarr = [n]
        if len(subarr) == 1:
            output.append(str(subarr[0]))
        elif len(subarr) > 1:
            output.append(str(subarr[0]) + "->" + str(subarr[-1]))
        return output