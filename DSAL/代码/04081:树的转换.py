def calculate_height(s):
    flag = [0]*10002  # 标记数组
    level, pre, post = 0, 0, 0  # 当前层数、最大层数、最大深度
    for char in s:  # 遍历字符串
        if char == "u":  # 如果字符为'u'
            level -= 1  # 层数减1
            flag[level] += 1  # 标记数组对应位置加1
        else:  # 如果字符为'd'
            level += 1  # 层数加1
            flag[level] = flag[level-1] + 1  # 标记数组对应位置等于上一层的标记数加1
            pre = max(level, pre)  # 更新最大层数
            post = max(post, flag[level])  # 更新最大深度
    return pre, post


s = input()  # 读取输入
pre, post = calculate_height(s)
print(f'{pre} => {post}')

# 这里需要自己在脑海里模拟一下，会方便理解。
