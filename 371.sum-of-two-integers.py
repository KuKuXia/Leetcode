#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.91%)
# Likes:    782
# Dislikes: 1374
# Total Accepted:    137.5K
# Total Submissions: 270.3K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: 3
#
#
#
# Example 2:
#
#
# Input: a = -2, b = 3
# Output: 1
#


class Solution(object):
    def getSum_1(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])

    def getSum(self, a, b):
        FILTER_32BIT = 0xffffffff

        while b & FILTER_32BIT:
            a, b = a ^ b, (a & b) << 1
        # bit cutoff needed only when carry overflows.
        # Otherwise use Python regular integer
        return a & FILTER_32BIT if b > FILTER_32BIT else a
