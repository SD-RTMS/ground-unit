from metrics_emitter import Emitter, emitter

METRICS_PREFIX = 'collector_service_'
RCVD_MSG_COUNT = METRICS_PREFIX + 'message_count'
DELAYED_MSG_COUNT = METRICS_PREFIX + 'delayed_message_count'
CHKSUM_ERROR_COUNT = METRICS_PREFIX + 'checksum_error_count'
PARSE_ERROR_COUNT = METRICS_PREFIX + 'parse_error_count'
INTERFACE_ERROR = METRICS_PREFIX + 'interface_error'

_receivedMessageCount = 0
_delayedMessageCount = 0
_checksumErrorCount = 0
_parseErrorCount = 0
_interfaceError = 0

def initMetricsZero():
    _receivedMessageCount = 0
    emitter().emit(RCVD_MSG_COUNT, _receivedMessageCount)
    _checksumErrorCount = 0
    emitter().emit(CHKSUM_ERROR_COUNT, _checksumErrorCount)
    _parseErrorCount = 0
    emitter().emit(PARSE_ERROR_COUNT, _parseErrorCount)
    _interfaceError = 0
    emitter().emit(INTERFACE_ERROR, _interfaceError)

def notifyMessageReceived():
    global _receivedMessageCount
    _receivedMessageCount += 1
    emitter().emit(RCVD_MSG_COUNT, _receivedMessageCount)

def notifyDelayedMessage():
    global _delayedMessageCount
    _delayedMessageCount += 1
    emitter().emit(DELAYED_MSG_COUNT, _delayedMessageCount)

def notifiyChecksumError():
    global _checksumErrorCount
    _checksumErrorCount += 1
    emitter().emit(CHKSUM_ERROR_COUNT, _checksumErrorCount)

def notifyParseError():
    global _parseErrorCount
    _parseErrorCount += 1
    emitter().emit(PARSE_ERROR_COUNT, _parseErrorCount)

def notifyInterfaceError():
    global _interfaceError
    _interfaceError += 1
    emitter().emit(INTERFACE_ERROR, _interfaceError)
