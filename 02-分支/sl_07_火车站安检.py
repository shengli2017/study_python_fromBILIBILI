# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 180
# 首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print("车票检查通过，准备开始安检")
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
    if knife_length > 20:

# 如果超过 20 厘米，提示刀的长度，不允许上车
        print("抱歉，您的刀长 %d 厘米，不允许上车" % knife_length)
# 如果不超过 20 厘米，安检通过
    else:
        print("恭喜您，安检通过")
# 如果没有车票，不允许进门
else:
    print("大哥，请先买票")

