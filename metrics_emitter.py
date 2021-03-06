import messages_pb2
import requests

#TODO
PUSHGATEWAY_HOST = 'emachine'

# Emits metrics to Prometheus PushGateway
class Emitter:
    job_name = 'rtms'
    instance_name = 'inst'
    _errorCount = 0

    def emit(self, msg: messages_pb2.SystemMetrics) -> bool:
        subsystems = {}
        delayStr = ''

        if msg.HasField("power_supply"):
            subsystems['power_supply'] = msg.power_supply
        if msg.HasField("computer"):
            subsystems['computer'] = msg.computer
        if msg.HasField("imu"):
            subsystems['imu'] = msg.imu
        if msg.HasField("digital"):
            subsystems['digital_io'] = msg.digital
        if msg.HasField("analog"):
            subsystems['analog_io'] = msg.analog
        
        if msg.delayed:
            delayStr = '_delayed'
            
        ec = 0

        for subsystem in subsystems:
            for descriptor in subsystems[subsystem].DESCRIPTOR.fields:
                value = getattr(subsystems[subsystem], descriptor.name)
                # pushgateway doesn't accept booleans
                if isinstance(value, bool):
                    value = int(value)
                #print ("%s: %s" % (subsystem + "_" + descriptor.name, value))

                ec += int(not self.emit((subsystem + "_" + descriptor.name + delayStr), value))

        return ec == 0

    def emit(self, key, value) -> bool:
        try:
            response = requests.post('http://' + PUSHGATEWAY_HOST + ':9091/metrics/job/{j}/instance/{i}'.format(j=self.job_name, i=self.instance_name), data='{k} {v}\n'.format(k=key, v=value), timeout=1.0)
            #print(response.status_code)
            return response.status_code == 200
        except:
            self._errorCount += 1
            return False

    def errorCount(self):
        return self._errorCount

_emitter = Emitter()
def emitter():
    return _emitter
