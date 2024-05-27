while True:
    try:
        num = input()
        if num[::-1] == num:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
