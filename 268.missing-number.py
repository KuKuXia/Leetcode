#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (48.43%)
# Likes:    940
# Dislikes: 1357
# Total Accepted:    286.3K
# Total Submissions: 588.9K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

import operator
from functools import reduce

class Solution(object):
    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in range(1, len(nums)):
            a ^= nums[i]
            a ^= i
        a ^= len(nums)
        return a

    def missingNumber_2(self, nums):
        # be careful about overflow
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

    def missingNumber(self, nums):
        return reduce(operator.xor, nums + range(len(nums) + 1))

    def missingNumber_4(self, nums):
        return (set(range(len(nums)+1)) - set(nums)).pop()