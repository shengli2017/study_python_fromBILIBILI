# 导入随机工具包
# 注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
# 因为，这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具
import random
# 从控制台输入要出的拳 —— 石头（1）/剪刀（2）/布（3）
player = int(input("玩家要出的拳头 - 石头（1）/剪刀（2）/布（3）是："))
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1,3)
print("玩家出的拳头是：%d - 电脑出的拳头是：%d" % (player,computer))
# 比较胜负
# 1 石头 胜 剪刀
# 2 剪刀 胜 布
# 3 布 胜 石头
# if () or () or ():
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑弱爆了！")
# 平局
elif player == computer:
    print("真是心有灵犀啊，再来一盘")

# 其他的情况就是电脑获胜
else:
    print("不服气，我们决战到天亮")