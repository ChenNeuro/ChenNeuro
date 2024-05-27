lst = list(map(int,input().split()))
odds = filter(lambda x: x%2==0,lst)
evens = filter(lambda x: x%2==1,lst)
l1 = list(evens)
l2 = list(odds)
l1.sort(reverse=True)
l2.sort()
ans = l1 + l2
print(*ans, sep=' ')