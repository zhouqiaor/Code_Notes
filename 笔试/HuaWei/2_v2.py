#coding=utf-8
import sys 
# 3,1,4,2
# 3

if __name__ == "__main__":
    line1 = sys.stdin.readline().strip().split(',')
    line2 = sys.stdin.readline().strip().split(',')
    A0 = [int(n) for n in line1]; A0.sort()
    B0 = [int(n) for n in line2]; B0.sort()
    if len(B0) == 1:
        result = max(B0[0] - A0[0], A0[-1] - B0[0])
        print(result)
    else:
        A = set(A0)
        i = 0
        while A:
            i += 1
            for b in B0:
                A.discard(b - i)
                A.discard(b + i)
        print(i)