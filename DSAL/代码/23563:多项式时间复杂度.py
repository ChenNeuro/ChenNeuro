string = list(map(str,input().split("+")))
bmax = 0
for i in string:
    if i[0] == "0":
        continue
    if i[0] == "n":
        i = "1" + i
    a,b = map(int,i.split("n^"))
    bmax = max(bmax,b)
print(f"n^{bmax}")