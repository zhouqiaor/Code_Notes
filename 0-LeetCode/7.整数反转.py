#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > -10 and x < 10:
            return x

        y = 0
        fo = 1
        if x < 0:
            fo = -1
            x = abs(x)
        lenX = len(str(abs(x)))
        for i in range(lenX):
            y = x % 10  + y * 10
            x //= 10
        y *= fo
        
        if y < 2**31 * -1 or y > 2**31 - 1:
            return 0
        else:
            return y
# @lc code=end

# 1032/1032 cases passed (28 ms)
# Your runtime beats 74.97 % of python submissions
# Your memory usage beats 6.45 % of python submissions (12.8 MB)