#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.03%)
# Likes:    2592
# Dislikes: 81
# Total Accepted:    330.4K
# Total Submissions: 804.2K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in nums:
            max_3_house_before, max_2_house_before, adjacent = max_2_house_before, adjacent, max(max_3_house_before + cur, max_2_house_before + cur)
        return max(max_2_house_before, adjacent)

