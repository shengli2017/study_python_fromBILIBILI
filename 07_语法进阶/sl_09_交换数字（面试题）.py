a = 6
b = 100

# 解法1：-使用其他变量
# c = a
# a = b
# b = c

# 解法2：-不适用其他变量
# a = a+b
# b = a-b
# a = a-b

# 解法3：-python 专有
# a, b = (b, a)
# 提示：等号右边是一个元组，只是把小括号省略了
a, b = b, a

print("a = %d" % a)
print("b = %d" % b)
