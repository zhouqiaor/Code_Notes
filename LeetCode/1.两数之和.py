#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # v1
        # 执行用时 : 4012 ms
        # 在所有 Python 提交中击败了 14.61% 的用户
        # 内存消耗 : 13.7 MB , 在所有 Python 提交中击败了 5.03% 的用户
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return[i,j]

        # v2
        # Your runtime beats 53.93 % of python submissions
        # Your memory usage beats 6.17 % of python submissions (14.2 MB)
        d = {}
        for i, n in enumerate(nums):
            if n in d.keys():
                return [d[n], i]
            else:
                d[target - n] = i
# @lc code=end

# 29/29 cases passed (392 ms)
if __name__ == "__main__":
    myTest = Solution()
    print(myTest.twoSum([2, 7, 11, 15], 9))