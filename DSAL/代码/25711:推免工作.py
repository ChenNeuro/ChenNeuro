import heapq
N, M = map(int, input().split())
GPA_number = []
heapq.heapify(GPA_number)
for _ in range(N):
    tmp = list(map(int,input().split()))
    number = tmp[0]
    grades_weight = tmp[1:].copy()
    GPA = 0
    total_weight = 0
    while grades_weight:
        weight = grades_weight.pop()
        total_weight += weight
        grade = grades_weight.pop()
        if grade >= 60:
            grade = 4 - 3 * (100 - grade) ** 2 / 1600
        else:
            grade = 0
        GPA += grade*weight
    heapq.heappush(GPA_number, (- GPA / total_weight, number))

ans = []
for i in range(M):
    ans.append(heapq.heappop(GPA_number)[1])

print(*ans)

