import math
n, m = map(int, input().split())
things = [[False for _ in range(m)] for _ in range(n)] ### [[False, False], [False, False]]
sale = [[] for _ in range(m)]
car = [0 for _ in range(m)]
#print(things)
#print(sale)

for i in range(n):
    temp = list(map(str, input().split()))
    for j in temp:
        store, price = map(int, j.split(':'))
        things[i][store-1] = price
#print(things)

for i in range(m):
    temp = list(map(str, input().split()))
    for j in temp:
        goal, temp_discount = map(int, j.split('-'))
        sale[i].append([goal, temp_discount])
#print(sale)

def discount(car):
    max_discount = 0
    for i_ in range(m):
        max_discount_temp = 0
        for j_ in sale[i_]:
            if car[i_] >= j_[0]:
                max_discount_temp = max(max_discount_temp,j_[1])
        max_discount += max_discount_temp
    return max_discount

minium = math.inf
def search(i, temp, things, sale):
    global minium
    if i == n:
        overall_discount = (temp//300)*50
        shop_discount = discount(car)
        minium = min(minium, temp-overall_discount-shop_discount)
    else:
        for j in range(m):
            if things[i][j]:
                car[j] += things[i][j]
                search(i+1, temp+things[i][j], things, sale)
                car[j] -= things[i][j]
search(0, 0, things, sale)
print(minium)
