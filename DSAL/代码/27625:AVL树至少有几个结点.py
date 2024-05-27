avl = [0, 1, 2]
for i in range(3, 50):
    avl.append(avl[i-2] + avl[i-1] + 1)
while True:
    try:
        n = int(input())
        print(avl[n])
    except:
        break