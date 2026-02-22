#/bin/python3
import socket

def port_scan():
    target_host=input('enter target host:')
    target_port=int(input('enter target port:'))
    result=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if result.connect_ex((target_host,target_port))==0:
        print(result + "is open")
    else:
        print("there are not open port on target")
    
if __name__=="__main__":
    port_scan()
