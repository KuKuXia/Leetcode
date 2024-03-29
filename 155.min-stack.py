#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (37.09%)
# Likes:    1849
# Dislikes: 195
# Total Accepted:    311.5K
# Total Submissions: 832.1K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Example:
#
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(x)
            self.min = x

        else:
            self.nums.append(x)
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        del self.nums[-1]
        if len(self.nums) >= 1:
            self.min = min(self.nums)
        else:
            self.min = None

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
