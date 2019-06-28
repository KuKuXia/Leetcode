#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (41.49%)
# Likes:    393
# Dislikes: 736
# Total Accepted:    159.8K
# Total Submissions: 383.4K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#
#
#

import re

class Solution(object):
    def reverseVowels_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

    def reverseVowels(self, s):
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
