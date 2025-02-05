from scapy.all import *


class PacketGenerator(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def simple_packet_(self, msg=None):
        if msg:
            this_packet = IP(dst=self.ip) / TCP(dport=self.port, flags='S') / Raw(load=msg)
        else:
            this_packet = IP(dst=self.ip) / TCP(dport=self.port, flags='S')
        return this_packet

    @staticmethod
    def send_packet_(pkt):
        send(pkt)

    @staticmethod
    def show_packet_(pkt):
        pkt.show()
