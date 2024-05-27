N = int(input())
word_to_docs = dict()
for i in range(N):
    words = input().split()[1:]
    for word in words:
        if word not in word_to_docs:
            word_to_docs[word] = set()
        word_to_docs[word].add(i+1)

# searching process
M = int(input())
for _ in range(M):
    query = input()
    if query in word_to_docs.keys():
        print(*sorted(word_to_docs[query]))
    else:
        print('NOT FOUND')
