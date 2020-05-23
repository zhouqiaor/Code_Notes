#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tran = {'I':1, 'V':5, 'X':10, 'L':50, 
                'C':100, 'D':500, 'M':1000,
                'II':2, 'III':3, 'IV':4, 'IX':9, 
                'XL':40, 'XC':90, 'CD':400, 'CM':900}
        if s in tran.keys():
            return tran[s]
        ro = 0
        while len(s):
            if len(s) >= 3 and s[0:3] in tran.keys():
                ro += tran[s[0:3]]
                s = s[3:]
                continue
            if len(s) >= 2 and s[0:2] in tran.keys():
                ro += tran[s[0:2]]
                s = s[2:]
                continue
            if len(s) >= 1 and s[0] in tran.keys():
                ro += tran[s[0]]
                s = s[1:]
        return ro

# @lc code=end
if __name__ == "__main__":
    myTest = Solution()
    print(myTest.romanToInt("III"))
    print(myTest.romanToInt("IV"))
    print(myTest.romanToInt("IX"))
    print(myTest.romanToInt("LVIII"))
    print(myTest.romanToInt("MCMXCIV"))
# 3999/3999 cases passed (180 ms)
# Your runtime beats 5.37 % of python submissions
# Your memory usage beats 5.88 % of python submissions (12.6 MB)