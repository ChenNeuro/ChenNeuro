n, x, y = map(int, input().split())
dic = dict()
for i in range(n):
    classname, name, score = map(str,input().split())
    if name in dic.keys():
        dic[name][0] += int(score)
        dic[name][1] += 1
    else:
        dic[name] = [int(score), 1]
q = int(input())
for i in range(q):
    name = input()
    if dic[name][1] >= x and (dic[name][0]/dic[name][1]) > y:
        print("yes")
    else:
        print("no")
