n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB = {}
for a in A:
    for b in B:
        if a + b not in AB:
            AB[a + b] = 1
        else:
            AB[a + b] += 1

count = 0
for c in C:
    for d in D:
        if -c - d in AB:
            count += AB[-c - d]
print(count)
