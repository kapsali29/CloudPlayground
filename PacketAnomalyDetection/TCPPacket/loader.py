import pyshark
from settings import TARGET_VARS


class PacketLoader(object):
    def __init__(self, pcap_path):
        self.pcap = pyshark.FileCapture(pcap_path)
        self.pcap_path = pcap_path

    @staticmethod
    def extract_layer(layer, attrs):
        return {field: layer.get(field) for field in attrs}

    @staticmethod
    def extract_frame_info(pkt):
        pkt_frame = pkt.frame_info
        return {
            "timestamp": pkt_frame.time, "pkt_len": pkt_frame.len,
            "pkt_captured_len": pkt.captured_length, "pkt_num": pkt_frame.number,
            "frame_time_delta": pkt_frame.time_delta, "protocols": pkt_frame.protocols
        }

    def process_pkt(self, pkt):
        pkt_info = {"frame": self.extract_frame_info(pkt)}
        for layer in pkt.layers:
            if layer.layer_name == "null" or layer.layer_name not in TARGET_VARS.keys():
                continue
            else:
                pkt_info[layer.layer_name] = self.extract_layer(layer, TARGET_VARS[layer.layer_name])
        return pkt_info

    def exec(self):
        pcap_info_list = [self.process_pkt(pkt) for pkt in self.pcap]
        return pcap_info_list
