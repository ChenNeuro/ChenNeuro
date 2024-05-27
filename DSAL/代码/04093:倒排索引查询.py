"""
N = int(input())
index = []
for _ in range(N):
    data = list(map(int, input().split()))
    index.append(set(data[1:]))


M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    result = set()
    for i, q in enumerate(query):
        if q == 0 or q == -1:
            continue
        if not result:
            result = index[i].copy()
        else:
            result &= index[i]
        if not result:
            break
    for i, q in enumerate(query):
        if q == 0 or q == 1:
            continue
        result -= index[i]

    if not result:
        print('NOT FOUND')
    else:
        print(' '.join(map(str, sorted((result)))))
"""


N = int(input())
index = {}
for i in range(1, N+1):
    data = list(map(int, input().split()))
    index[i] = set(data[1:])

M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    result = set()
    deresult = set()
    for i, q in enumerate(query, start=1):
        if q == -1:
            deresult |= index[i]
            continue
        elif q == 0:
            continue
        if not result:
            result = index[i].copy()
        else:
            result &= index[i]
        if not result:
            break
    result -= deresult
    if result:
        print(' '.join(map(str, sorted(result))))
    else:
        print('NOT FOUND')