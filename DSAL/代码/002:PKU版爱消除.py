S = input()
Stack = []
for i in S:
    Stack.append(i)
    if len(Stack) >= 3 and (Stack[-3] == "P" and Stack[-2] == "K" and Stack[-1] == "U"):
        Stack.pop()
        Stack.pop()
        Stack.pop()
print("".join(Stack))