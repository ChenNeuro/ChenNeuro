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
        if Left[i] >= Right[j]:
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
    k = 0
    try:
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        MergeSort(arr)
        print(k)
        print()
    except:
        exit()

