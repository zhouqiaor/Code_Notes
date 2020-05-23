#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        lens = [len(s) for s in strs]
        min_lens = min(lens)
        if min_lens == 0:
            return ''
        com = 0
        for i in range(min_lens):
            ls = []
            for s in strs:
                ls.append(s[i])
            if len(set(ls)) == 1:
                com += 1
            else:
                break
        return strs[0][0:com]


# @lc code=end
if __name__ == "__main__":
    myTest = Solution()
    print(myTest.longestCommonPrefix(["flower","flow","flight"]))
    print(myTest.longestCommonPrefix(["dog","racecar","car"]))

# 118/118 cases passed (24 ms)
# Your runtime beats 64.69 % of python submissions
# Your memory usage beats 5.88 % of python submissions (12.7 MB)