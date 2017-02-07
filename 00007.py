while 1:
    height = float(input("请输入身高"))
    weight = float(input("请输入体重"))
    BMI = height / weight**2
    if BMI < 18.5:
        print("过轻", BMI)
        break
    elif 18.5 < BMI < 25:
        print("正常")
    else:
        print("死胖子")
print("nihao ")