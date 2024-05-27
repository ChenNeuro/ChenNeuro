N = int(input())
arr = [list(map(int, input().split("."))) for i in range(N)]
arr.sort()
for i in arr:
    print(".".join(map(str, i)))