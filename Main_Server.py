import socket
import sys
from queue import Queue


NUMBER_OF_THREADS = 2
NUMBER_OF_JOBS = [1,2]
queue = Queue()
all_connections = []
all_addresses = []
name="Server : "

def create_socket():
    try:
        global host
        global port
        global server_socket
        host=socket.gethostname()
        port=3000
        server_socket=socket.socket()
    except socket.error as err:
        print("Socket Creation Error With Message : "+str(err))


def bind_port():
    try:
        global host
        global port
        global server_socket
        server_socket.bind((host,port))
        server_socket.listen(5)
        print("Socket Has Been Binded On Computer(default IP) : "+host+" on Port : "+str(port))
    except socket.error as err:
        print("Socket Binding Error With Message : "+ str(err)+"  ********RETRYING...********")
        bind_port()

def start_listening():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while True:
        try:
            conn,address = server_socket.accept()
            server_socket.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("A New Device Connected Recently on IP : "+address[0]+ " Using Port : "+str(address[1]))
            send_messages(conn)
            #conn.close()
        except socket.error as err:
            print("An Error Occured While Accepting A Connection With Message : "+str(err))
def send_messages(conn):
    msg=name+"Hello, You Have been Connected In conference.... WELLCOME (By Server)"
    for a in all_connections:
        a.send(bytes(msg.encode("utf-8")))
def listen_for_messages():
    message=server_socket.recv(1024).decode()
    print(message.split()[0])

def main():
    create_socket()
    bind_port()
    start_listening()
main()
