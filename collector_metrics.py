from metrics_emitter import Emitter, emitter

METRICS_PREFIX = 'collector_service_'
RCVD_MSG_COUNT = METRICS_PREFIX + 'message_count'
DELAYED_MSG_COUNT = METRICS_PREFIX + 'delayed_message_count'
CHKSUM_ERROR_COUNT = METRICS_PREFIX + 'checksum_error_count'
PARSE_ERROR_COUNT = METRICS_PREFIX + 'parse_error_count'
INTERFACE_ERROR = METRICS_PREFIX + 'interface_error'
EMIT_ERROR_COUNT = METRICS_PREFIX + 'http_error_count'

_receivedMessageCount = 0
_delayedMessageCount = 0
_checksumErrorCount = 0
_parseErrorCount = 0
_interfaceError = 0

def initMetricsZero():
    global _receivedMessageCount, _delayedMessageCount, _checksumErrorCount, _parseErrorCount, _interfaceError
    _receivedMessageCount = 0
    _checksumErrorCount = 0
    _parseErrorCount = 0
    _interfaceError = 0
    return emitAllMetrics()

def emitAllMetrics():
    global _receivedMessageCount, _delayedMessageCount, _checksumErrorCount, _parseErrorCount, _interfaceError
    ec = False
    ec &= _emit(RCVD_MSG_COUNT, _receivedMessageCount)
    ec &= _emit(CHKSUM_ERROR_COUNT, _checksumErrorCount)
    ec &= _emit(PARSE_ERROR_COUNT, _parseErrorCount)
    ec &= _emit(INTERFACE_ERROR, _interfaceError)
    ec &= _emit(EMIT_ERROR_COUNT, emitter().errorCount())
    return ec

def notifyMessageReceived():
    global _receivedMessageCount
    _receivedMessageCount += 1
    return _emit(RCVD_MSG_COUNT, _receivedMessageCount)

def notifyDelayedMessage():
    global _delayedMessageCount
    _delayedMessageCount += 1
    return _emit(DELAYED_MSG_COUNT, _delayedMessageCount)

def notifiyChecksumError():
    global _checksumErrorCount
    _checksumErrorCount += 1
    return _emit(CHKSUM_ERROR_COUNT, _checksumErrorCount)

def notifyParseError():
    global _parseErrorCount
    _parseErrorCount += 1
    return _emit(PARSE_ERROR_COUNT, _parseErrorCount)

def notifyInterfaceError():
    global _interfaceError
    _interfaceError += 1
    return _emit(INTERFACE_ERROR, _interfaceError)

def notifyEmitError():
    return _emit(EMIT_ERROR_COUNT, emitter().errorCount())
    
def _emit(key, value):
    return emitter().emit(key, value)
