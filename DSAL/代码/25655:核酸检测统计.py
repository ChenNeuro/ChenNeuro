from collections import defaultdict
n = int(input())
m = int(input())
numbers = []
numbers_date = defaultdict(list)
numbers_college = dict()
college_volume = defaultdict(int)
college_failure = defaultdict(int)
college_failure_fre = defaultdict(int)


for student in range(n):
    number, collage = list(map(int, input().split()))
    numbers.append(number)
    numbers_college[number] = collage
    college_volume[collage] += 1


for time in range(m):
    date, number = list(map(int, input().split()))
    numbers_date[number].append(date)

for number in numbers:
    dates = numbers_date[number]
    dates.sort()
    collage = numbers_college[number]

    if dates[0] != 1:
        college_failure[collage] += 1
        college_failure_fre[collage] += 1 / college_volume[collage]

    else:
        test = [False]*13

        for i in dates:
            for j in [0, 1, 2]:
                test[i + j] = True
        if not all(test[1:10]):
            college_failure[collage] += 1
            college_failure_fre[collage] += 1 / college_volume[collage]


# print(college_failure_fre)
print(sum(college_failure.values()))
print(max(college_failure_fre, key=college_failure_fre.get))
