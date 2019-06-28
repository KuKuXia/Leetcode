#
# @lc app=leetcode id=405 lang=python
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.92%)
# Likes:    268
# Dislikes: 72
# Total Accepted:    48.5K
# Total Submissions: 115.5K
# Testcase Example:  '26'
#
#
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two's complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#
#
#


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        tot = ""
        if num == 0:
            return "0"
        if num < 0:
            num = 0xffffffff + 1 + num
        while num:
            num, adding = divmod(num, 16)
            tot += str(adding if adding <
                       10 else unichr(ord('a') + (adding % 10)))
        return tot[::-1]
