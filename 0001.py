member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
count = 0
length = len(member)   # 计算member长度
while count < length:   # 循环输出直到长度
    print(member[count], member[count + 1])  # 打印member和后面数字
    count += 2  # 跳两步
