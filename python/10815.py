import sys
input = sys.stdin.readline

M = int(input())
card = set(list(map(int,input().split())))
N = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    if i in card:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

# import sys
# input = sys.stdin.readline

# M = int(input())
# card = list(map(int,input().split()))
# N = int(input())
# card2 = list(map(int, input().split()))

# _dict = {}

# for i in range(len(card)):
#     _dict[card[i]] = 0

# for j in range(N):
#     if  card2[j] in _dict:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')



# //시간 초과
# import sys
# input = sys.stdin.readline

# M = int(input())
# card = sorted(list(map(int,input().split())))
# N = int(input())
# card2 = sorted(list(map(int, input().split())))

# for i in card2:
#     if i in card:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')

# import sys
# input = sys.stdin.readline

# M = int(input())
# card = set(list(map(int,input().split())))
# N = int(input())
# card2 = set(list(map(int, input().split())))

# for i in card2:
#     if i in card:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')