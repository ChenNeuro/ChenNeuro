
k = 0
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    Mid = len(lists)//2
    Left_lists = MergeSort(lists[:Mid])
    Right_lists = MergeSort(lists[Mid:])
    return Merge(Left_lists,Right_lists)

def Merge(Left,Right):
    global k
    Sortedlist = []
    i, j = 0, 0
    while i < len(Left) and j < len(Right):
        # print(i,j)
        if Left[i] <= Right[j]:
            Sortedlist.append(Left[i])
            i += 1
        else:
            Sortedlist.append(Right[j])
            k += len(Left) - i
            j += 1
        # print((Left,Right),k)
    Sortedlist += Left[i:]
    Sortedlist += Right[j:]
    # print(Sortedlist,k)
    return Sortedlist


while True:
    n = int(input())
    if n == 0:
        break
    else:
        k = 0
        arr = [int(input()) for _ in range(n)]
        MergeSort(arr)
        print(k)


"""
217986354
while True:
    n = int(input())
    if n == 0:
        break
    else:
        k = 0
        arr = [int(input()) for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > arr[j]:
                    k += 1
        print(k)


import bisect
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr = [0]*n
        k = 0
        for i in range(n-1, -1, -1):
            arr[i] = int(input())
        lst = []
        for j in range(n):
            k += bisect.bisect_left(lst, arr[j])
            bisect.insort_left(lst, arr[j])
        print(k)
"""