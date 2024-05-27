n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n or arr[k-1] < arr[k]:
    print(arr[k-1])
else:
    print(-1)