class Solution(object):
    # 循环暴力求解 超出时间限制
    def maxScore(self, cardPoints, k):
        maxS = 0
        for i in range(k):
            S = sum(cardPoints[:i] + cardPoints[i-k:])
            maxS = max(maxS, S)
        maxS = max(maxS, sum(cardPoints[0:k]))
        return maxS

    def maxScore2(self, cardPoints, k):
        sumC = sum(cardPoints)
        minW = sumC
        l = len(cardPoints)
        for i in range(k):
            W = sum(cardPoints[i:i-k])
            minW = min(minW, W)
        minW = min(minW, sum(cardPoints[k:]))
        return sumC-minW

sl = Solution()
print(sl.maxScore([1,2,3,4,5,6,1], 3))
print(sl.maxScore([2,2,2], 2))
print(sl.maxScore([96,90,41,82,39,74,64,50,30], 8))

print(sl.maxScore2([1,2,3,4,5,6,1], 3))
print(sl.maxScore2([2,2,2], 2))
print(sl.maxScore2([96,90,41,82,39,74,64,50,30], 8))
print(sl.maxScore2([1,1000,1], 1))