def calculateZ(string):
    Z = [0] * len(string)
    Z[0] = len(string)
    left, right = 0, 0
    for i in range(1, len(string)):
        if i > right:
            left, right = i, i
            while right < len(string) and string[right - left] == string[right]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            k = i - left
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < len(string) and string[right - left] == string[right]:
                    right += 1
                Z[i] = right - left
                right -= 1
    return Z

def calculatePeriods(string):
    Z = calculateZ(string)
    periods = []
    for i in range(1, len(string)):
        if Z[i] + i == len(string):
            periods.append(i)
    return periods

string = input().strip()
periods = calculatePeriods(string)+[len(string)]
print(' '.join(map(str, periods)))
