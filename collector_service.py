import interface
from metrics_emitter import Emitter, emitter
from message_deserializer import ReceivedMessage
import collector_metrics as cm

interface = interface.defaultInterface()

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
            emitter().emit(metrics)

if __name__ == '__main__':
    cm.initMetricsZero()

    ## Attempt to open the interface
    interfaceOpened = False
    try:
        interfaceOpened = interface.open()
    except:
        pass

    if not interfaceOpened:
        cm.notifyInterfaceError()
        exit(1)

    try:
        while 1:
            poll()
    except KeyboardInterrupt:
        print('Exiting...')
        interface.close()
        exit(0)
