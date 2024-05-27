# print(str(oct(int(input())))[2:])

num = int(input())
stack = []
while num:
    stack.append(num%8)
    num = num//8
    # print(num)
print("".join(str(_) for _ in stack[::-1]))