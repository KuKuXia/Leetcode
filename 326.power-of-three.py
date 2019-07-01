#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.66%)
# Likes:    286
# Dislikes: 1050
# Total Accepted:    188.7K
# Total Submissions: 452.4K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#


class Solution(object):
    def isPowerOfThree_1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThree_2(self, n):
        # power_list
        power_list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147,
                      531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        return n in power_list
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return True if n == 1 else False
