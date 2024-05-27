import itertools
n = list(map(str,input()))
n.sort()
for i in itertools.permutations(n,len(n)):
    print(''.join(j for j in i))