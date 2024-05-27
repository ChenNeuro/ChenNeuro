x = int(input())
if x % 2 != 0 or x < 6:
    print("Error!")
else:
    prime = [False] * 2001
    prime_list = []
    ans = []
    for i in range(2,2001):
        if not prime[i]:
            prime_list.append(i)
            for j in range(i,2001,i):
                prime[j] = True
    for i in prime_list:
        if x - i in prime_list and x - i >= i:
            ans.append(f"{x}={i}+{x-i}")
    for i in ans:
        print(i)