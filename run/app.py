import pyshark
from run.packet_manager import PacketManager



class Analyze_Capture:

    def __init__(self):
        self._file_location = None
        self._capture = None
        self.packet_manager = PacketManager()

    def load_capture(self, file_location):
        self._file_location = file_location

        try:
            capture = pyshark.FileCapture(file_location)
            self._capture = capture
        except:
            return False

        try:
            self.read_capture()
            self._capture.close()
        except:
            return False

        self.packet_manager.read_packet(30)

    def read_capture(self):
        for packet in self._capture:
            self.packet_manager.add_packet(packet)


if __name__ == '__main__':

    analyze_capture = Analyze_Capture()
    analyze_capture.load_capture('pcap.pcapng')