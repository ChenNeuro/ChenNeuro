for turn in range(int(input())):
    coin_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0}
    left = []
    right = []
    result = []
    for i in range(3):
        a, b, c = map(str, input().split())
        left.append(a)
        right.append(b)
        result.append(c)
    tag = False
    for _ in coin_dict.keys():
        if tag:
            break
        for i in [1,-1]:
            coin_dict[_] = i
            tag = True
            for j in range(3):
                if not tag:
                    break
                left_weight, right_weight = 0, 0
                for k in range(len(left[j])):
                    left_weight += coin_dict[left[j][k]]
                    right_weight += coin_dict[right[j][k]]

                if result[j] == "even" and left_weight != right_weight:
                    tag = False
                    break
                elif result[j] == "up" and left_weight <= right_weight:
                    tag = False
                    break
                elif result[j] == "down" and left_weight >= right_weight:
                    tag = False
                    break

            if tag:
                if coin_dict[_] < 0:
                    print(f'{_} is the counterfeit coin and it is light.')
                if coin_dict[_] > 0:
                    print(f'{_} is the counterfeit coin and it is heavy.')
                break
            else:
                coin_dict[_] -= i
