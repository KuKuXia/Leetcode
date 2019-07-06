#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (61.21%)
# Likes:    1117
# Dislikes: 85
# Total Accepted:    138.2K
# Total Submissions: 225.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
#
#
#
# Example:
#
#
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
#
#
#
#


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        unvisited: -1 visiting: 1 visited: 2 idea:
        Everytime we encounter a new island(unvisited: -1), result += 4(Each island has 4 sides)
        On the path of visting(visiting: 1), when we meet visited island(visited: 2) or water(grid: 0), return directly; when we meet the island on current visiting path(visiting: 1), result -= 2(overlapping sides)
        """

        m, n = len(grid), len(grid[0])
        visited = [[-1 for i in range(n)] for j in range(m)]  # -1: unvisited
        self.res = 0

        def dfs(i, j):
            outOfRange = i < 0 or i >= m or j < 0 or j >= n
            if outOfRange or visited[i][j] == 2 or grid[i][j] == 0:
                return
            if visited[i][j] == 1:   # 1: meet the island on the path of visiting
                # if 2 edges are connected with each other, we need to get rid of the overlaping edges (total_edges = 4 + 4 - 2)
                self.res -= 2
                return
            self.res += 4    # one cell has 4 edges
            visited[i][j] = 1    # mark it as visiting
            for a, b in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                dfs(i + a, j + b)
            visited[i][j] = 2         # 2: visited
            return

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return self.res
