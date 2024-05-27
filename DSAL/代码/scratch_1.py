T = int(input())
S = list(map(int, input().split()))
tag = "NO"

def check(array, target):
    global tag
    if target == 1:
        tag = "YES"
        return
    for pos, i in enumerate(array):
        if T % i == 0:
            a = array.pop(pos)
            check(array, target // i)
            if tag == "YES":
                break
            array.append(a)
        else:
            continue
    return


check(S, T)
print(tag)