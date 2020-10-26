import messages_pb2

class Emitter:
    def emit(self, msg: messages_pb2.SystemMetrics):
        with open('/tmp/metrics.prom', 'w') as f:
            f.write('computer_power_voltage ' + str(msg.computer.power_voltage) + '\n')
            f.write('computer_power_current ' + str(msg.computer.power_current) + '\n')
            f.write('computer_temperature_die ' + str(msg.computer.temperature_die) + '\n')
