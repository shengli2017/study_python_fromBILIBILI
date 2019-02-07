for num in [1, 2, 3]:

    print(num)
    if num == 2:

        break

else:
    """
    如果循环体内部使用break推出了循环
    else 下方的代码就不会被执行
    """
    print("会执行吗？")

print("循环结束")