import serial
from socket import socket, AF_INET, SOCK_STREAM
import sys

class Interface:
    def open(self) -> bool:
        return NotImplementedError

    def close(self) -> bool:
        return NotImplementedError

    def dataWaiting(self) -> bool:
        return NotImplementedError

    def getBufferedData(self) -> bytes:
        return NotImplementedError

    def waitData(self) -> bool:
        return NotImplementedError

## Used for testing
class DummyInterface(Interface):
    def open(self):
        print('Start dummy')
        return True

    def close(self):
        print('Stop dummy')
        return True

    def dataWaiting(self):
        return False

    def getBufferedData(self):
        return bytes([])

    def waitData(self):
        return True

class SerialInterface(Interface):
    def __init__(self):
        # TODO replace SERIAL PORT with the correct port
        self.serial = serial.Serial("SERIAL PORT", 115200, timeout=1.0)
        self._dataWaiting = False

    def open(self):
        return True

    def close(self):
        self.serial.close()

    def dataWaiting(self):
        return self._dataWaiting

    def getBufferedData(self):
        self._dataWaiting = False
        return self.buffer

    def waitData(self):
        try:
            self.buffer = self.serial.read()
            print('Received data')
            self._dataWaiting = True
            return True
        except:
            print(sys.exc_info())
            return False 

## Basic TCP client
class TCPInterface(Interface):
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.buffer = bytes([])
        self._dataWaiting = False

    def open(self):
        print('Start TCP')
        try:
            dest = ('127.0.0.1', 1234)
            self.sock.connect(dest)
            return True
        except:
            print(sys.exc_info())
            return False

    def close(self):
        print('Stop TCP')
        try:
            self.sock.close()
            return True
        except:
            print(sys.exc_info())
            return False

    def dataWaiting(self):
        return self._dataWaiting

    def getBufferedData(self):
        self._dataWaiting = False
        return self.buffer

    def waitData(self):
        try:
            self.buffer = self.sock.recv(2048)
            print('Received data')
            self._dataWaiting = True
            return True
        except:
            print(sys.exc_info())
            return False

def defaultInterface() -> Interface:
    return SerialInterface()
