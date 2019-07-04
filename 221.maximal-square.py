#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (33.05%)
# Likes:    1347
# Dislikes: 34
# Total Accepted:    135K
# Total Submissions: 405K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#
#


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i, r in enumerate(matrix):
            r = matrix[i] = list(map(int, r))
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(matrix[i - 1][j], r[j - 1],
                               matrix[i - 1][j - 1]) + 1
        return max(map(max, matrix + [[0]])) ** 2
