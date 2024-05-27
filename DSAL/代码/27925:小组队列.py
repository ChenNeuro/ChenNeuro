from collections import deque

t = int(input())
teams = {i: deque(map(int, input().split())) for i in range(t)}
team_member = {person: i for i, team in teams.items() for person in team}
queue = deque()
group_queue = {i: deque() for i in range(t)}


while True:
    command = input().split()
    if command[0] == 'STOP':
        break
    elif command[0] == 'ENQUEUE':
        person = int(command[1])
        if person in team_member:
            i = team_member[person]
            group_queue[i].append(person)
            if i not in queue:
                queue.append(i)
        else:
            t += 1
            group_queue[t] = deque([person])
            queue.append(t)
    elif command[0] == 'DEQUEUE':
        group = queue[0]
        print(group_queue[group].popleft())
        if not group_queue[group]:
            queue.popleft()
