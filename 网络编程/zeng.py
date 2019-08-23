#!/usr/bin/python3
import socket, time
import threading
# 目标地址IP/URL及端口
target_host = "127.0.0.1"
target_port = 6666
# 创建一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接主机
client.connect((target_host,target_port))
def handle_send():
    while True:
        content = input("zeng40:")
        client.send(content.encode())
        if b"exit" in content.encode():
            client.close()
            print("退出！")
            break
def handle_receive():
    while True:
        response = client.recv(2048)
        now = time.strftime("%H:%M ", time.localtime())
        print ("\n%swan50:"%now + response.decode())
        if "exit" in response.decode():
            client.close()
            print("退出！")
            break
send_handler = threading.Thread(target=handle_send,args=())
receive_handler = threading.Thread(target=handle_receive,args=())
send_handler.start()
receive_handler.start()