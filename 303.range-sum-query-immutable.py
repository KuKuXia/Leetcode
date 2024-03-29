#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (38.00%)
# Likes:    471
# Dislikes: 780
# Total Accepted:    141.8K
# Total Submissions: 369.6K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

