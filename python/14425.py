import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = [input() for _ in range(N)]

count = 0

for _ in range(M):
    T = input()    
    if T in S:
        count += 1
print(count)