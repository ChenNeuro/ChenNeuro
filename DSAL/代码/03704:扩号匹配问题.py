while True:
    try:
        string = input()
        stack_l = []
        stack_r = []
        for char in range(len(string)):
            if string[char] == "(":
                stack_l.append(char)
            elif string[char] == ")":
                if len(stack_l) > 0:
                    stack_l.pop()
                else:
                    stack_r.append(char)
        ans = [" "]*len(string)
        for i in range(len(stack_l)):
            ans[stack_l[i]] = "$"
        for i in range(len(stack_r)):
            ans[stack_r[i]] = "?"
        print(string)
        print("".join(ans))
    except EOFError:
        break