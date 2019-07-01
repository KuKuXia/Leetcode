#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (31.66%)
# Likes:    1224
# Dislikes: 64
# Total Accepted:    95K
# Total Submissions: 298.6K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Now suppose you are given
# the locations and height of all the buildings as shown on a cityscape photo
# (Figure A), write a program to output the skyline formed by these buildings
# collectively (Figure B).
# ⁠   
# 
# The geometric information of each building is represented by a triplet of
# integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
# right edge of the ith building, respectively, and Hi is its height. It is
# guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
# may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
# point is the left endpoint of a horizontal line segment. Note that the last
# key point, where the rightmost building ends, is merely used to mark the
# termination of the skyline, and always has zero height. Also, the ground in
# between any two adjacent buildings should be considered part of the skyline
# contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3
# 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# 
# The number of buildings in any input list is guaranteed to be in the range
# [0, 10000].
# The input list is already sorted in ascending order by the left x position
# Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
# acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...[2 3], [4 5], [12 7], ...]
# 
# 
#

from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点
        # 所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点

        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H)、第二种是轮廓降低事件(R, 0)
        # 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # 先根据L从小到大排序、再根据H从大到小排序(记录为-H的原因)
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort()

        # 保存返回结果
        res = [[0, 0]]

        # 最小堆，保存当前最高的轮廓(-H, R)，用-H转换为最大堆，R的作用是记录该轮廓的有效长度
        live = [(0, float("inf"))]

        # 从左至右遍历关键事件
        for L, negH, R in events:

            # 如果是轮廓升高事件，记录到最小堆中
            if negH:
                heappush(live, (negH, R))

            # 获取当前最高轮廓
            # 根据当前遍历的位置L，判断最高轮廓是否有效
            # 如果无效则剔除，让次高的轮廓浮到堆顶，继续判断
            while live[0][1] <= L:
                heappop(live)

            # 如果当前的最高轮廓发生了变化，则记录一个关键点
            if res[-1][1] != -live[0][0]:
                res += [[L, -live[0][0]]]
        return res[1:]

