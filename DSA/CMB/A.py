import sys

N = int(sys.stdin.readline().strip())
lines=[]
for i in range(N):
    line = sys.stdin.readline().strip()
    line_split = line.split(' ')
    line_int = [int(l) for l in line_split]
    lines.append(line_int)
print(lines)

# Sum = 0
# for line in lines:
#     Sum = Sum + line[0]