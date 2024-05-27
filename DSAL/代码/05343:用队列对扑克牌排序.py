n = int(input())
cards = list(map(str, input().split()))
QUEUE = [[] for i in range(14)]
for card in cards:
    number = card[1]
    QUEUE[int(number)].append(card)
i = 0
for queue in QUEUE[1:10]:
    i += 1
    print(f'Queue{i}:{" ".join(queue)}')
    if queue:
        for card in queue:
            color = card[0]
            QUEUE[int(color.lower(), 16)].append(card)

ans = []
i = 0
arr = "ABCD"
for queue in QUEUE[10:]:
    print(f'Queue{arr[i]}:{" ".join(queue)}')
    ans.extend(queue)
    i += 1
print(*ans)