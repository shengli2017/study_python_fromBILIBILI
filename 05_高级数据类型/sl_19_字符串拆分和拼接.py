
# 假设：一下内容是从网络上抓取得
# 要求：
# 1. 将字符串中的空白字符全部去掉
# 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 如穷千里目 \n更上一层楼"

print(poem_str)

# 1. 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 2. 合并字符串
poem_str = " ".join(poem_list)
print(poem_str)
