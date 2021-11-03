# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:32:04 2021

@author: virustous
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find proper row
        r = len(matrix) - 1
        while r >= 0:
            if matrix[r][0] <= target:
                break
            r -= 1
            
        # check if this row contains target by means of binary search
        cleft = 0
        cright = len(matrix[r]) - 1
        while cleft <= cright:
            cmid = (cleft + cright) // 2
            if matrix[r][cmid] == target:
                return True
            elif matrix[r][cmid] > target:
                cright = cmid - 1
            else:
                cleft = cmid + 1
        return False