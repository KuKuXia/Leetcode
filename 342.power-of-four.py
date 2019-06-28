#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (40.27%)
# Likes:    318
# Dislikes: 148
# Total Accepted:    116K
# Total Submissions: 287.2K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&(num-1) == 0 and len(bin(num)[3:])%2 == 0

