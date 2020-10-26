import messages_pb2

class ReceivedMessage:
    def __init__(self, rawBytes: bytes):
        self._checksum = int.from_bytes(rawBytes[0:2], 'little')
        self._dataLength = int.from_bytes(rawBytes[2:4], 'little')
        self._data = rawBytes[4:]

        self._calculatedChecksum = self.calculateChecksum()
        self._proto = None

        print('Checksum ' + str(self._checksum))
        print('Calculated ' + str(self._calculatedChecksum))
        print('Length ' + str(self._dataLength))

        if self.valid():
            print('Valid')
            self._proto = messages_pb2.SystemMetrics()
            self._proto.ParseFromString(self._data)

    def valid(self) -> bool:
        #return self._checksum == self._calculatedChecksum
        return True

    def checksum(self) -> int:
        return self._checksum

    ## Calculates BSD 16-bit checksum
    def calculateChecksum(self) -> int:
        chksum = 0

        for i in range(min(self._dataLength, len(self._data))):
            chksum = (chksum >> 1) + ((chksum & 1) << 15)
            chksum += self._data[i]
            chksum &= 0xFFFF
        
        return chksum

    def dataLength(self) -> int:
        self._dataLength

    def get(self) -> messages_pb2.SystemMetrics:
        return self._proto
