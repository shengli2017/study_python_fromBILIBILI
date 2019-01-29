name = "小明"

# Python 解释器知道下方定义了一个函数


def say_hello():
    """打招呼
    函数上方应该保留两个空行，函数注释应该放在函数下方"""
    print("hello 1")
    print("hello 2")
    print("hello 3")

print(name)

# 只有在程序中，主动调用函数，才会让函数执行
say_hello()

print(name)