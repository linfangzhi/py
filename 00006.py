def 计数(*param):
    length = len(param)
    for i in range(length):
        字母 = 0
        空格 = 0
        数字 = 0
        其他 = 0
        for each in param[i]:
            if each.isalpha():
                字母 += 1
            elif each.isdigit():
                数字 += 1
            elif each == ' ':
                空格 += 1
            else:
                其他 += 1
        print("字母%d个，空格%d个，数字%d个，其他%d个" % (字母, 空格, 数字, 其他))

str = input("请输入字符串")
print(计数(str))