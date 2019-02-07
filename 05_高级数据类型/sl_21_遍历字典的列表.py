students = [
    {"name" : "小明"},
    {"name" : "小红"}
]

# 在学院列表中搜索指定的姓名
find_name = "张三"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s" % find_name)
        # 如果已经找到，应该直接退出循环，而不再便利后续的元素
        break

    # else:
    #
    #     print("抱歉没有找到 %s" % find_name)
else:
#     # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
#     # 还希望得到一个统一的提示！
    print("抱歉没有找到 %s" % find_name)


print("循环结束")