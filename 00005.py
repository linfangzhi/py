def 回文(desStr):
    desStrfan = desStr[::-1]
    if desStr == desStrfan:
        return 1
    else:
        return 0
while 1:
    desStr = input("请输入一句话\n")
    if 回文(desStr) == 1:
        print("是回文\n")
    else:
        print("不是回文\n")
