def Dec2Bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2  # 取余
        dec = dec // 2  # 地板除
        temp.append(quo)

    while temp:
        result += str(temp.pop())  # 移除最后的一个字符

    return result

Dec2Bin1 = input("heiheihei")
a = int(Dec2Bin1)
print(Dec2Bin(a))
