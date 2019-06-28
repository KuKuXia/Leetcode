#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (48.05%)
# Likes:    541
# Dislikes: 56
# Total Accepted:    99.5K
# Total Submissions: 206.6K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        odd_exist = False
        total = 0
        for k, v in count.items():
            if v % 2 == 0:
                total += v
            else:
                odd_exist = True
                total += v - 1
        return total + 1 if odd_exist else total

