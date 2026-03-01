import socket
import os
from ctypes import *
import struct
import sys
import ipaddress
host=input('enter host for sniff:')
class IP:
    _fields_=[
        ("ihl",c_ubyte,4),

        ("version",c_ubyte,4),

        ("tos",c_ubyte,8),
        ("len", c_ushort,16),

        ("id",c_ushort, 16),
        ("offset", c_ushort,16),

        ("ttl",c_ubyte,8),
        ("protocol_num",c_ubyte, 8),
        ("sum",c_ushort, 16),

        ("src",c_uint32, 32),

        ("dst", c_uint32, 32),
    ]
    def __new__(cls,socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)
    def __init__(self,socket_buffer=None):
        #human readable IP ADRESSES:
        self.src_adress=socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_adress=socket.inet_ntoa(sturct.pack("<L",self.dst))
    def sniff(host):
        if os.name=='nt':
            socket_protocol=socket.IPPROTO_IP
        else:
            socket_protocol=socket.IPPROTO_ICMP
        sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
        sniffer.bind((host,0))
        sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
        if os.name=='nt':
            sniffer.ioctl(socket.SIO_RCVALL,socket.RECVALL_ON)
        try:
            while True:
                raw_buffer=sniffer.recvfrom(65535),[0]
                ip_header=ip(raw_buffer[0:20])
                print('Protocol: %s %s -> %s' %(
                    ip_header.protocol,
                    ip_header.src_adress,
                    ip_header.dst_adress))
                
        except KeyboardInterrupt:
            if os.name=='nt':
                sniffer.ioctl(socket.SIO_RECVALL,socket.RECVALL_OFF)
            sys.exit()
    
    if __name__=='__main__':
        if len(sys.argv)==2:
            host=sys.argv[1]
        else:
            sniff(host)