import re
string = input()
pattern = r"\w*h\w*e\w*l\w*l\w*o\w*"
matches = re.match(pattern, string)
if matches:
    print("YES")
else:
    print("NO")