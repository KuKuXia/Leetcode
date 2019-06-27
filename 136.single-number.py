#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (60.18%)
# Likes:    2528
# Dislikes: 95
# Total Accepted:    477.7K
# Total Submissions: 789.9K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]
        for i in range(1, len(nums)):
            single ^= nums[i]
        return single
