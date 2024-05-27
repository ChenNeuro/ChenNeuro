def solve(a, b):
    l = r = 0
    while a != 1 and b != 1:
        if a > b:
            quotient = a // b
            a -= quotient * b
            l += quotient
        else:
            quotient = b // a
            b -= quotient * a
            r += quotient
    return (l + a - 1, r + b - 1)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    l, r = solve(a, b)
    print(f"Scenario #{i+1}:")
    print(f"{l} {r}\n")