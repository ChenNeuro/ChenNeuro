n = 0
while True:
    p, e, i, d = map(int,input().split())
    if p == -1 and e == -1 and i == -1 and d == -1:
        break
    n += 1
    a = 1
    while 4*a % 23 != p % 23:
        a += 1

    a1 = 28*33*a
    b = 1
    while 3*b % 28 != e % 28:
        b += 1

    b1 = 23*33*b
    c = 1
    while 17*c % 33 != i % 33:
        c += 1

    c1 = 23*28*c
    ans = (a1+b1+c1-1)%(21252)+1-d
    while ans <= 0:
        ans += 21252
    print(f'Case {n}: the next triple peak occurs in {ans} days.')