n = int(1e4)
prime = [False]*(n+1)
prime[0] = False
prime[1] = True
ans_list = set()
for i in range(2,n+1):
    if not prime[i]:
        for j in range(i*i,n+1,i):
            prime[j] = True
for i in range(2,n+1):
    if not prime[i]:
        ans_list.add(i*i)
#print(ans_list)
m, n = map(int, input().split())
for i in range(m):
    temp = 0
    score = list(map(int, input().split()))
    for j in score:
        if j in ans_list:
            temp += j
    if temp == 0:
        print(0)
    else:
        print("%.2f" % (temp/len(score)))