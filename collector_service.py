import interface
from metrics_emitter import Emitter
from message_deserializer import ReceivedMessage

interface = interface.defaultInterface()
emitter = Emitter()

## Polling loop
def poll():
    ## Synchronous wait for data arrival
    if not interface.waitData():
        return

    if interface.dataWaiting():
        buf = interface.getBufferedData()

        msg = ReceivedMessage(buf)

        if msg.valid():
            metrics = msg.get()
            print(metrics)
            emitter.emit(metrics)

if __name__ == '__main__':
    ## Attempt to open the interface
    if not interface.open():
        exit(1)

    try:
        while 1:
            poll()
    except KeyboardInterrupt:
        print('Exiting...')
        interface.close()
        exit(0)
