string = input().lower()
tmp = ""
for i in string:
    if i not in ('a','o','y','e','u','i'):
        tmp += i
print('.'+".".join(tmp))