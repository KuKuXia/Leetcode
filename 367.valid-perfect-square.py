#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.80%)
# Likes:    463
# Dislikes: 107
# Total Accepted:    114K
# Total Submissions: 285.2K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
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
# Input: 14
# Output: false
#


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        x, i = 0, 1
        while x < num:
            x += i
            i += 2
        return x == num
