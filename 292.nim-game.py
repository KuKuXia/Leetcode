#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.63%)
# Likes:    376
# Dislikes: 1161
# Total Accepted:    186K
# Total Submissions: 334K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# Example:
# 
# 
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be 
# removed by your friend.
#
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if (n % 100 and n % 4) else False

