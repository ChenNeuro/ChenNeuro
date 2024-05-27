import hashlib


def md5_hash(s):
    return hashlib.md5(s.encode()).hexdigest()


T = int(input())
for _ in range(T):
    s1 = input().strip()
    s2 = input().strip()
    if md5_hash(s1) == md5_hash(s2):
        print("Yes")
    else:
        print("No")