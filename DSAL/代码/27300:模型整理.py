n = int(input())
dic = dict()
for i in range(n):
    name, params = input().split("-")
    if name in dic.keys():
        if params[-1] == "M":
            dic[name][0].append(params)
        else:
            dic[name][1].append(params)
    else:
        if params[-1] == "M":
            dic[name] = [[params], []]
        else:
            dic[name] = [[], [params]]

ans_l = []
for name, params in dic.items():
    params[0].sort(key=lambda x:float(x[:-1]))
    params[1].sort(key=lambda x:float(x[:-1]))
    # print(params)
    ans = f"{name}: "
    tmp = []
    for m in params[0]:
        tmp.append(m)
    for b in params[1]:
        tmp.append(b)
    ans += ", ".join(tmp)
    ans_l.append(ans)
ans_l.sort()
for i in ans_l:
    print(i)