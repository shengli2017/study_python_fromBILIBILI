# 1. 打开文件
file = open("README", encoding="UTF-8")

# 2. 读取文件内容
text = file.read()
print(text)

# 3. 关闭文件
file.close()