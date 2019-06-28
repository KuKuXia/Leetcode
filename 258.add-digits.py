#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (54.12%)
# Likes:    465
# Dislikes: 798
# Total Accepted:    241.7K
# Total Submissions: 445.3K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution(object):
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum([int(i) for i in list(str(num))])
        return num
    
    def addDigits(self, num):
        return num if num == 0 else num % 9 or 9
