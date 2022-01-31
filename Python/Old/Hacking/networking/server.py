import socket
import threading


HEADER= 64
PORT= 8080
SERVER= socket.gethostbyname(socket.gethostname())
# SERVER='192.168.43.247'
print(SERVER)
ADDR = (SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected .")
    connected= True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg =conn.recv(msg_length).decode(FORMAT)

            if msg== DISCONNECT_MESSAGE:
                connected=False

            print(f'[{addr}] {msg }')
            conn.send("Msg receive".encode(FORMAT))


    conn.close()


def start():
    print(f'[LISTENING] Server is listening on {SERVER}')
    server.listen()
    while True:
        conn,addr=server.accept()   # getting information from new connection
        tread=threading.Thread(target=handle_client,args={conn,addr})
        tread.start()
        print(f"[ACTIVE CONNECTION]{threading.active_count()-1}")


print("[STARTING] server is starting ...!")
start()


