# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#X
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
# ##########################################
while 1:
    symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '1234567890'

    password = input("请输入密码")
    # 判断长度
    length = len(password)

    while (password.isspace() or length == 0):
        password = input("你的输入有误")
    if length <= 8:
        flag_len = 1
    elif 8 < length < 16:
        flag_len = 2
    else:
        flag_len = 3

    # 判断字符
    flag_con = 0
    for each in password:
        if each in symbols:
            flag_con += 1
            break

    # 判断字母
    for each in password:
        if each in chars:
            flag_con += 1
            break

    # 打印结果
    while 1:
        print("你的密码的安全评定级别为：", end='')
        if flag_len == 1 or flag_con ==1:
            print("低")
        elif flag_con == 2 or flag_len ==2:
            print("中")
        else:
            print("高")
        break


