a = int(input())
if a % 4 == 0:
    if a % 100 == 0 and a % 400 != 0:
        print("N")
        exit()
    if a % 3200 == 0:
        print("N")
        exit()
    print("Y")
else:
    print("N")