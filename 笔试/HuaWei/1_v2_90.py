#coding=utf-8
import datetime
# test = 1980 01 02 5|1980 01 04
if __name__ == "__main__":
    data1, data2 = input().strip().split('|')

    weekday1 = int(data1[-2:])
    data1 = data1[:-2]

    year1_len = len(data1.split(' ')[0])
    if year1_len < 4:
        data1 = (4 - year1_len) * '0' + data1

    year2_len = len(data1.split(' ')[0])
    if year2_len < 4:
        data2 = (4 - year2_len) * '0' + data2

    c = datetime.datetime.strptime(data2, '%Y %m %d') - datetime.datetime.strptime(data1, '%Y %m %d')
    result = (c.days) + weekday1 % 7
    result = result % 7
    if result == 0:
        print(7)
    else:
        print(result)