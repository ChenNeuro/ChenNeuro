n = int(input())
output = "*"*(3**n)


def delete(s, n):
    if n == 0:
        return s
    else:
        left = delete(s[:len(s)//3], n-1)
        mid = "-"*(len(s)//3)
        right = delete(s[2*len(s)//3:], n-1)
        return left + mid + right


print(delete(output, n))
