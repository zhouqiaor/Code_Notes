#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        sT = s[::-1]
        if s == sT:
            return True
        else:
            return False
# @lc code=end

# 11509/11509 cases passed (104 ms)
# Your runtime beats 85.6 % of python submissions
# Your memory usage beats 7.14 % of python submissions (12.6 MB)
