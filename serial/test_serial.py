# import serial.tools.list_ports
# port_list = list(serial.tools.list_ports.comports())
# print(len(port_list))
# if len(port_list) == 0:
#    print('无可用串口')
# else:
#     for i in range(0,len(port_list)):
#         print(port_list[i])

#
# import serial
# import time
#
# def recv(serial):
#     while True:
#         data = serial.read_all()
#         if data == '':
#             continue
#         else:
#             break
#     return data
#
# if __name__ == '__main__':
#     serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)  #/dev/ttyUSB0
#     if serial. :
#         print("open success")
#     else :
#         print("open failed")
#
#     while True:
#         data =recv(serial)
#         if data != b'' :
#             print("receive : ",data)
#             serial.write(data) #数据写回

#导入模块
import serial ,time
#端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx="/dev/ttyUSB0"
#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=5
# 打开串口，并得到串口对象
ser=serial.Serial("/dev/ttyUSB0", 115200)
#读串口的信息(不用自己手动打开串口终端，会报错)
while True:
    line = ser.read(1024)
    print(line.decode('utf-8'))
    if b'exit' in line:
        break
ser.close()

# #向串口里面写信息
# a = ser.write(b'enable\n')
# print(a)
# time.sleep(1)
# b = ser.write(b'show running-config\n')
# print(b)
#
# ser.close()