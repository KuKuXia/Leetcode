#
# @lc app=leetcode id=149 lang=python
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.78%)
# Likes:    486            
# Dislikes: 1333
# Total Accepted:    122K
# Total Submissions: 770.3K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        l = len(points)

        if l <= 2:
            return l

        res = 0

        for i in range(l):
            point_num = {}
            p_max, overlap = 0, 0
            for j in range(i+1, l):
                dx, dy = points[j][0] - points[i][0], points[j][1]-points[i][1]
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue

                # calculate the gcd, or the slope of a line
                gcd_value = self.gcd(dx, dy)
                dx /= gcd_value
                dy /= gcd_value
                # Using gcd as the key in the map, no precision problem
                key = str(dx) + 'gcd' + str(dy)
                # if key not in point_num, return the default value: 0, then add 1
                point_num[key] = point_num.setdefault(key, 0) + 1
                # find the current max value
                p_max = max(p_max, point_num[key])
                # find the maximum number of points in all lines
            res = max(res, p_max + overlap + 1)
        return res

    # calculate the gcd of two numbers
    def gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a % b)
