n = int(input())
string = input()
ans = ""
for i in range(n):
    for j in range(len(string)//n):
        if not j%2:
            ans += string[n*j+i]
        else:
            ans += string[n*(j+1)-i-1]
print(ans)