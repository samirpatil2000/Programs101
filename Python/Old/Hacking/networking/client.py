import socket


HEADER= 64
PORT= 8080
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
SERVER= socket.gethostbyname(socket.gethostname())
#SERVER='192.168.43.247'
ADDR = (SERVER,PORT)


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length = len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=  b' ' *(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

send("Hello Samir Patil")
# print("a = Message \n x = Disconnect ")
# user=input("Enter Message")
# send(user)
# a=input("Enter message !")
# while user != 'a':
#     if (user=='a'):
#         msg=input("Enter Message :")
#         send(msg)
print("Enter 0 for quite\n")
for _ in range(0,1000):
    q=int(input("Option:"))
    while q != 0:
        msg=input("Your Message :\n")
        send(msg)
    else:
        break







