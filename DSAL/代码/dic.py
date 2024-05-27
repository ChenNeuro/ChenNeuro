from collections import defaultdict
dic = defaultdict(int)
input_string = input("Enter")
for i in input_string:
    dic[i] += 1
for i in dic.items():
    print(i)