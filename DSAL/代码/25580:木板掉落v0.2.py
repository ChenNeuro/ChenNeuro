H, L, n = map(int, input().split())
V = list(map(float, input().split()))
V.sort()
if n % 2 == 1:
    v = V[n//2]
else:
    v = V[n//2]
t = L/v
l = H - 0.5*10*(t**2)
print("%.2f" % l)
