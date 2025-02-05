from TCPPacket.gen import PacketGenerator

this_gen = PacketGenerator(ip='127.0.0.1', port=5000)
pkt = this_gen.simple_packet_(msg="monique eisai vroma")
this_gen.send_packet_(pkt)
