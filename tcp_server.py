import socket 
import threading
IP='0.0.0.0'
port=9998
def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(IP,port)
    server.listen(5)
    print(f'Listening on {IP}:{port}')
    while True:
        client,adress=server.accept()
        print(f'Acceptet request by {adress[0]},{adress[1]}')
        client_handler=threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        request=sock.recv(1024)
        print(f'recieved a infotmation : {request.decode("utf-8")}')
if __name__=='__main__':
    main()