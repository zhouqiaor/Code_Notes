import sys
# input()
# sys.stdin.readline().strip()

def LZH():
    s_input = str(sys.stdin.readline().strip())
    ss = s_input.split('5a')
    ss = list(filter(None, ss))
    answer = '5a'
    for s in ss:
        tmp = s.replace('5b ba', '5a')
        tmp = tmp.replace('5b bb', '5b')
        tmp = tmp.split(' ')
        tmp = list(filter(None, tmp))
        if len(tmp) == int(tmp[-1]) + 1:
            answer = answer + s + '5a'
        del tmp
    print(answer)


def SWJ():
    N = int(sys.stdin.readline().strip())
    lines=[]
    for i in range(N):
        line = sys.stdin.readline().strip()
        line_split = line.split(' ')
        line_int = [int(l) for l in line_split]
        lines.append(line_int)
    print(lines)

if __name__=="__main__":
    while True:
        ss = sys.stdin.readline().split()
        if len(ss)==0:
            break
        print(" ".join(sorted(ss)))

    l = sys.stdin.readline()
    l = int(l)
    ss = sys.stdin.readline().split()
    print(" ".join(sorted(ss)))