class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        # marked_1 = []
        ls = [int(n) for n in s]
        for i in range(len(ls)-1):
            # if ls[i] == 0 and ls[i+1] == 0:
            # if ls[i] == 1 and ls[i+1] == 1:
            score_ = i+1 - sum(ls[:i+1]) + sum(ls[i+1:])
            score = max(score, score_)
        return score

sl = Solution()
print(sl.maxScore('011101'))
print(sl.maxScore('00111'))
print(sl.maxScore('1111'))
