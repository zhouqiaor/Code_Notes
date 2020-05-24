#coding=utf-8
import sys 
from datetime import datetime
import calendar
# 1980 01 02 5|1980 01 04

if __name__ == "__main__":
    d1, d2 = sys.stdin.readline().strip().split('|')
    D1 = list(map(int, d1.split(' ')))
    D2 = list(map(int, d2.split(' ')))
    w1 = D1.pop()

    c = calendar.weekday(D2[0], D2[1], D2[2]) - calendar.weekday(D1[0], D1[1], D1[2])
    result = (c + w1) % 7
    if result == 0:
        print(7)
    else:
        print(result)