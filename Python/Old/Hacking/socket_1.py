import socket

HEADER= 64
PORT= 5050

SERVER='192.168.43.247'
ADDR = (SERVER,PORT)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(ADDR)
ans=s.recv(1048)
print(ans)


print("Hello I'm Samir ")







