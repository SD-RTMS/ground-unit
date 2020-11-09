import messages_pb2
import requests

#TODO
PUSHGATEWAY_HOST = 'localhost'

# Emits metrics to Prometheus PushGateway
class Emitter:
    job_name = 'rtms'
    instance_name = 'inst'

    def emit(self, msg: messages_pb2.SystemMetrics):
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

        for subsystem in subsystems:
            for descriptor in subsystems[subsystem].DESCRIPTOR.fields:
                value = getattr(subsystems[subsystem], descriptor.name)
                #print ("%s: %s" % (subsystem + "_" + descriptor.name, value))

                response = requests.post('http://' + PUSHGATEWAY_HOST + ':9091/metrics/job/{j}/instance/{i}'.format(j=self.job_name, i=self.instance_name), data='{k} {v}\n'.format(k=(subsystem + "_" + descriptor.name + delayStr), v=value))
                #print(response.status_code)
