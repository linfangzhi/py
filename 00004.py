def 出现(des, sub):
    count = 0
    length = len(des)
    if sub not in des:
        print("找不到啊")
    else:
        for each1 in range(length-1):
            if des[each1] == sub[0]:
                if des[each1+1] == sub[1]:
                    count += 1
        print("字符出现%d次" % count)
des = input("请输入字符串\n")
sub = input("子字符串")
出现(des, sub)