string = input()
tmp = ""
ans = ""
for i in string:
    tmp += i
    if int(tmp,2) % 5:
        ans += "0"
    else:
        ans += "1"

print(ans)