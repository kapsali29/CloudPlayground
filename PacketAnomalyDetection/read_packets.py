from TCPPacket.loader import PacketLoader

pl = PacketLoader(pcap_path="sample.pcap")
for pkt in pl.pcap:
    print(pkt)
    # pkt_info = pl.process_pkt(pkt)
    # print(pl)
