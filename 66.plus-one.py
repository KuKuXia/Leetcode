#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.25%)
# Likes:    886
# Dislikes: 1584
# Total Accepted:    404.4K
# Total Submissions: 978K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            sum += digits[i] * pow(10, len(digits) - i - 1)
        return [int(i) for i in str(sum+1)]

    def plusOne_two(self, digits: List[int]) -> List[int]:
        bit = 1
        for i in range(len(digits)):
            tmp = digits[len(digits) - 1 - i] + bit
            if tmp > 9:
                bit = 1
                digits[len(digits) - 1 - i] = (tmp % 9) -1
            else:
                digits[len(digits) - 1 - i] = tmp
                bit = 0
            if bit == 0 or i == len(digits) - 1:
                if bit == 1:
                    digits.insert(0,1)
                break
        return digits
            
