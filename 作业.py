number = input("我现在在想的数字")
flag = 0
number = int(number)
print(type(number))
while not isinstance(number, int):
    print("输入错误")
    number = input("在理")
    number = int(number)
while flag == 0:
    if number == 10:
       print("666")
       break
    if number < 10:
        print("小了")
    if number > 10:
        print("大了")
    number = input("再来一次")
    number = int(number)
print("结束")
