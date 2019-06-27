#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (32.03%)
# Likes:    906
# Dislikes: 1347
# Total Accepted:    442.6K
# Total Submissions: 1.4M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in [None, ""] or haystack == needle:
            return 0
        length = len(needle)
        if len(haystack) < length:
            return - 1
        for i in range(len(haystack) - length+1):
            if haystack[i: i + length] == needle:
                return i
        return -1
