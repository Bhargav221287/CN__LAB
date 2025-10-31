class Packet:
    def __init__(self, source_ip, dest_ip, payload, priority):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload
        self.priority = priority

def fifo_scheduler(packet_list: list) -> list:
    return packet_list

def priority_scheduler(packet_list: list) -> list:
    return sorted(packet_list, key=lambda p: p.priority)
packets = [
        Packet("A", "B", "Data Packet 1", 2),
        Packet("A", "B", "Data Packet 2", 2),
        Packet("A", "B", "VOIP Packet 1", 0),
        Packet("A", "B", "Video Packet 1", 1),
        Packet("A", "B", "VOIP Packet 2", 0)
]
fifo_result = [p.payload for p in fifo_scheduler(packets)]
priority_result = [p.payload for p in priority_scheduler(packets)]
print(fifo_result)
print(priority_result)

