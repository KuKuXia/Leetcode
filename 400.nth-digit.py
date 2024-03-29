#
# @lc app=leetcode id=400 lang=python
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.31%)
# Likes:    260
# Dislikes: 842
# Total Accepted:    48.5K
# Total Submissions: 159.4K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        m, stage = 1, 9
        while n > stage:
            n = n-stage
            m = m+1
            stage = 9*m*(10**(m-1))
        num = 10**(m-1)+(n-1)//m
        index = (n-1) % m
        return int(str(num)[index])

