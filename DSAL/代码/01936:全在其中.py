while True:
    try:
        s, t = input().split()
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
            if i == len(s):
                break
        print("Yes" if i == len(s) else "No")
    except EOFError:
        break
