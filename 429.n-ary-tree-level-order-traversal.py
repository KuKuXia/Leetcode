#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (59.50%)
# Likes:    257
# Dislikes: 31
# Total Accepted:    35.6K
# Total Submissions: 59.5K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
#
#
#
#
#
#
# We should return its level order traversal:
#
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# Note:
#
#
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
#
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # Set first node or None in case of empty case
        queue = [root] if root else []
        result = []  # Results will be stored here

        # As long as there are any items in queue
        while queue:
            # Add value of every nodes in queue
            result.append([node.val for node in queue])

            # For every node in queue and its children
            queue = [child for node in queue for child in node.children]

        return result
