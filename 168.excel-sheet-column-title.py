#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.99%)
# Likes:    735
# Dislikes: 145
# Total Accepted:    175K
# Total Submissions: 601.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#
#


class Solution(object):
    def convertToTitle(self, num):
        """
        :type num: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)
