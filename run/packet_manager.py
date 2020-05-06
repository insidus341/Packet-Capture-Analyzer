class PacketManager:

    def __init__(self):
        self.packets = []

    def add_packet(self, packet):
        Packet(packet)
        self.packets.append(packet)

    def read_packet(self, number):
        try:
            packet = self.packets[number]
            print(packet.number)
        except:
            return False


class Packet:

    def __init__(self, packet):
        self._packet = packet

    def get_packet(self):
        return self._packet
