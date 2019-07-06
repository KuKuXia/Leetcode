#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (40.06%)
# Likes:    819
# Dislikes: 100
# Total Accepted:    82.6K
# Total Submissions: 206.1K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
#
#
#
# Example 1:
#
#
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#
#
# Example 2:
#
#
# Input: "aba"
# Output: False
#
#
# Example 3:
#
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
#
#
#

import re


class Solution:
    def repeatedSubstringPattern_1(self, s: str) -> bool:
        l = len(s)
        for i in range(l):
            time = l // (i + 1)
            if time == 1:
                break
            a = s[:i+1] * time
            if a == s:
                return True
        return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        return True if re.match(r'(\w+)\1+$', s) else False
