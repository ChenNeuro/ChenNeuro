def oneMove(n, source, target):
    print(f"{n}:{source}->{target}")

def Hanoi(n, source, aux, target):
    if n == 1:
        oneMove(n, source, target)
    else:
        Hanoi(n-1, source, target, aux)
        oneMove(n, source, target)
        Hanoi(n-1, aux, source, target)


n, a, b, c = map(str, input().split())
Hanoi(int(n), a, b, c)