string = input()
opt = []
s = ""
turn = 0
for i in range(len(string)):
    if string[i] == "(":
        opt.append(i)
        turn += 1
    elif string[i] == ")":
        left = opt.pop()
        # print(left, i)
        string = string[:left] + " " + string[left+1:i][::-1] + " " + string[i+1:]
        turn -= 1
print("".join(string.split()))