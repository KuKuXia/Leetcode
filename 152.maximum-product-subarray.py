#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.27%)
# Likes:    2158
# Dislikes: 102
# Total Accepted:    217.5K
# Total Submissions: 738.7K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        current_max, current_min, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            tmp = current_max
            current_max = max(n, n*current_max, n*current_min)
            current_min = min(n, n * tmp, n * current_min)
            ans = max(ans, current_max)
        return ans
