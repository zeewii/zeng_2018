#!/usr/bin/python3
import socket, time
import threading

# 监听的IP及端口
bind_ip = "127.0.0.1"
bind_port = 6666
#socket 服务器初始化--创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定要监听的地址和端口
server.bind((bind_ip, bind_port))
#监听端口，等待连接的最大数量是5
server.listen(5)
print ("----开始监听%s:%d" % (bind_ip, bind_port))



#阻塞在这里，等待接收客户端的数据
#接受一个新的连接，client_socket是接收的客户端的数据，addr是客户端的地址和端口组成的元组
client_socket, addr = server.accept()
print ("----从:%s:%d接收连接" % (addr[0],addr[1]))

# 定义函数handle_client,输入参数client_socket
def handle_client():
    while True:
        request = client_socket.recv(1024)
        now = time.strftime("%H:%M ", time.localtime())
        print ("\n%szeng40:"%now + request.decode())
        if "exit" in request.decode():
            server.close()
            client_socket.close()
            print("zeng40退出！")
            break

def handle_send():
    while True:
        content = input("wan50:")
        client_socket.send(content.encode())
        if b"exit" in content.encode():
            server.close()
            client_socket.close()
            print("退出！")
            break

#创建一个线程
client_handler = threading.Thread(target=handle_client,args=())
send_handler = threading.Thread(target=handle_send,args=())
client_handler.start()
send_handler.start()