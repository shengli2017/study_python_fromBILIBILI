def sum_2_num(num1, num2):
    """函数的返回值"""

    return num1 + num2
num1 = int(input("请输入第一个相加数："))
num2 = int(input("请输入第二个相加数："))
result = sum_2_num(num1, num2)
print("两个数相加等于：%d" % result)