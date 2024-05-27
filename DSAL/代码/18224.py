square = [x**2 for x in range(1,100)]
ans_list = set()
for i in square:
    for j in square:
        ans_list.add(i + j)
input()
number = list(map(int,input().split()))
for j in number:
    if j in ans_list:
        print(bin(j), oct(j), hex(j))