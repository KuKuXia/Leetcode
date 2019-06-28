#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (46.02%)
# Likes:    910
# Dislikes: 68
# Total Accepted:    231.1K
# Total Submissions: 499.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def binaryTreePaths_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # dfs + stack
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res

    def binaryTreePaths_2(self, root):
        # dfs + queue
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, ls + str(node.val) + "->"))
        return res

    def binaryTreePaths(self, root):
        # dfs recursively
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + "->", res)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + "->", res)
