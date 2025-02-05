# PACKETS FEATURES TO KEEP from WireShark
TARGET_VARS = {
    "tcp": ["srcport", "dstport", "seq", "ack", "flags", "len", "checksum", "window_size_value"],
    "ip": ["addr", "dst", "version", "ttl", "len", "proto", "hdr_len", "dsfield_ecn", "frag_offset", "dsfield_dscp"],
    "tls": ["record_content_type", "record_length", "record_version"],
    "udp": ["checksum", "dstport", "length", "srcport", "time_delta"],
    "ssdp": ["http_host", "http_request", "http_request_uri"]
}
