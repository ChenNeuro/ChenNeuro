'''
for i in itertools.count(1,2):
    print(i)
'''


import itertools

for i in itertools.chain("abc", "def"):
    print(f"{i}\n")
print("\n---------------------------\n")

for key, group in itertools.groupby("aaAbBdbadAadcc", lambda x: x.upper()):
    print(key, list(group))
    "A['a', 'a', 'A'] B['b', 'B'] D['d'] B['b'] A['a'] D['d'] A['A', 'a'] D['d'] C['c', 'c']"

print("\n---------------------------\n")

for i in itertools.accumulate([0, 1, 0, 2, 3, 4, 5, 8], max):
    print(i)
    "01123458"
print("\n---------------------------\n")

for i in itertools.product([0, 1, 2], [0, 2, 4], [0, 3, 6]):
    print(i)
print("\n---------------------------\n")

for i in itertools.permutations("abc", 2):
    print(i)  # ('a', 'b')('a', 'c')('b', 'a')('b', 'c')('c', 'a')('c', 'b')

print("\n---------------------------\n")

for i in itertools.combinations(["a", "b", "c"], 2):
    print(i)  # ('a', 'b')('a', 'c')('b', 'c')

print("\n---------------------------\n")
for i in itertools.combinations_with_replacement("abc", 2):
    print(i)  # ('a', 'a')('a', 'b')('a', 'c')('b', 'b')('b', 'c')('c', 'c')
