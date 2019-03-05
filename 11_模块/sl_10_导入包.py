import sl_message

sl_message.send_message.send("hello")
txt = sl_message.receive_message.receive()
print(txt)
