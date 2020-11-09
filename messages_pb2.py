# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='downlink_proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0emessages.proto\x12\x0e\x64ownlink_proto\"o\n\x0e\x44igitalMetrics\x12\x11\n\tdigital_0\x18\x01 \x01(\x08\x12\x11\n\tdigital_1\x18\x02 \x01(\x08\x12\x11\n\tdigital_2\x18\x03 \x01(\x08\x12\x11\n\tdigital_3\x18\x04 \x01(\x08\x12\x11\n\tdigital_4\x18\x05 \x01(\x08\"W\n\rAnalogMetrics\x12\x10\n\x08\x61nalog_0\x18\x01 \x01(\x02\x12\x10\n\x08\x61nalog_1\x18\x02 \x01(\x02\x12\x10\n\x08\x61nalog_2\x18\x03 \x01(\x02\x12\x10\n\x08\x61nalog_3\x18\x04 \x01(\x02\"c\n\tTimestamp\x12\r\n\x05month\x18\x01 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\x0c\n\x04hour\x18\x04 \x01(\x05\x12\x0e\n\x06minute\x18\x05 \x01(\x05\x12\x0e\n\x06second\x18\x06 \x01(\x05\"j\n\x12PowerSupplyMetrics\x12\x16\n\x0etemperature_v0\x18\x01 \x01(\x02\x12\x16\n\x0etemperature_v1\x18\x02 \x01(\x02\x12\x11\n\tlevel_3v3\x18\x03 \x01(\x02\x12\x11\n\tlevel_5v0\x18\x04 \x01(\x02\"\xcb\x02\n\nIMUMetrics\x12\x0f\n\x07\x65uler_x\x18\x01 \x01(\x02\x12\x0f\n\x07\x65uler_y\x18\x02 \x01(\x02\x12\x0f\n\x07\x65uler_z\x18\x03 \x01(\x02\x12\x0e\n\x06quat_a\x18\x04 \x01(\x02\x12\x0e\n\x06quat_b\x18\x05 \x01(\x02\x12\x0e\n\x06quat_c\x18\x06 \x01(\x02\x12\x0e\n\x06quat_d\x18\x07 \x01(\x02\x12\x0f\n\x07omega_x\x18\x08 \x01(\x02\x12\x0f\n\x07omega_y\x18\t \x01(\x02\x12\x0f\n\x07omega_z\x18\n \x01(\x02\x12\x15\n\rlinearAccel_x\x18\x0b \x01(\x02\x12\x15\n\rlinearAccel_y\x18\x0c \x01(\x02\x12\x15\n\rlinearAccel_z\x18\r \x01(\x02\x12\x13\n\x0bmagnitude_x\x18\x0e \x01(\x02\x12\x13\n\x0bmagnitude_y\x18\x0f \x01(\x02\x12\x13\n\x0bmagnitude_z\x18\x10 \x01(\x02\x12\x13\n\x0btemperature\x18\x11 \x01(\x02\"]\n\x14SpaceComputerMetrics\x12\x15\n\rpower_voltage\x18\x01 \x01(\x02\x12\x15\n\rpower_current\x18\x02 \x01(\x02\x12\x17\n\x0ftemperature_die\x18\x03 \x01(\x02\"\xc4\x02\n\rSystemMetrics\x12\'\n\x04time\x18\x01 \x01(\x0b\x32\x19.downlink_proto.Timestamp\x12\x0f\n\x07\x64\x65layed\x18\x02 \x01(\x08\x12\x38\n\x0cpower_supply\x18\x03 \x01(\x0b\x32\".downlink_proto.PowerSupplyMetrics\x12\x36\n\x08\x63omputer\x18\x04 \x01(\x0b\x32$.downlink_proto.SpaceComputerMetrics\x12\'\n\x03imu\x18\x05 \x01(\x0b\x32\x1a.downlink_proto.IMUMetrics\x12/\n\x07\x64igital\x18\x06 \x01(\x0b\x32\x1e.downlink_proto.DigitalMetrics\x12-\n\x06\x61nalog\x18\x07 \x01(\x0b\x32\x1d.downlink_proto.AnalogMetricsb\x06proto3')
)




_DIGITALMETRICS = _descriptor.Descriptor(
  name='DigitalMetrics',
  full_name='downlink_proto.DigitalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digital_0', full_name='downlink_proto.DigitalMetrics.digital_0', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital_1', full_name='downlink_proto.DigitalMetrics.digital_1', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital_2', full_name='downlink_proto.DigitalMetrics.digital_2', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital_3', full_name='downlink_proto.DigitalMetrics.digital_3', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital_4', full_name='downlink_proto.DigitalMetrics.digital_4', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=145,
)


_ANALOGMETRICS = _descriptor.Descriptor(
  name='AnalogMetrics',
  full_name='downlink_proto.AnalogMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analog_0', full_name='downlink_proto.AnalogMetrics.analog_0', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analog_1', full_name='downlink_proto.AnalogMetrics.analog_1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analog_2', full_name='downlink_proto.AnalogMetrics.analog_2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analog_3', full_name='downlink_proto.AnalogMetrics.analog_3', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=234,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='downlink_proto.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='month', full_name='downlink_proto.Timestamp.month', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='downlink_proto.Timestamp.day', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='downlink_proto.Timestamp.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='downlink_proto.Timestamp.hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='downlink_proto.Timestamp.minute', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='downlink_proto.Timestamp.second', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=335,
)


_POWERSUPPLYMETRICS = _descriptor.Descriptor(
  name='PowerSupplyMetrics',
  full_name='downlink_proto.PowerSupplyMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature_v0', full_name='downlink_proto.PowerSupplyMetrics.temperature_v0', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature_v1', full_name='downlink_proto.PowerSupplyMetrics.temperature_v1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_3v3', full_name='downlink_proto.PowerSupplyMetrics.level_3v3', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_5v0', full_name='downlink_proto.PowerSupplyMetrics.level_5v0', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=443,
)


_IMUMETRICS = _descriptor.Descriptor(
  name='IMUMetrics',
  full_name='downlink_proto.IMUMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='euler_x', full_name='downlink_proto.IMUMetrics.euler_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='euler_y', full_name='downlink_proto.IMUMetrics.euler_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='euler_z', full_name='downlink_proto.IMUMetrics.euler_z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quat_a', full_name='downlink_proto.IMUMetrics.quat_a', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quat_b', full_name='downlink_proto.IMUMetrics.quat_b', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quat_c', full_name='downlink_proto.IMUMetrics.quat_c', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quat_d', full_name='downlink_proto.IMUMetrics.quat_d', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omega_x', full_name='downlink_proto.IMUMetrics.omega_x', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omega_y', full_name='downlink_proto.IMUMetrics.omega_y', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omega_z', full_name='downlink_proto.IMUMetrics.omega_z', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linearAccel_x', full_name='downlink_proto.IMUMetrics.linearAccel_x', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linearAccel_y', full_name='downlink_proto.IMUMetrics.linearAccel_y', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linearAccel_z', full_name='downlink_proto.IMUMetrics.linearAccel_z', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnitude_x', full_name='downlink_proto.IMUMetrics.magnitude_x', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnitude_y', full_name='downlink_proto.IMUMetrics.magnitude_y', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnitude_z', full_name='downlink_proto.IMUMetrics.magnitude_z', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='downlink_proto.IMUMetrics.temperature', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=777,
)


_SPACECOMPUTERMETRICS = _descriptor.Descriptor(
  name='SpaceComputerMetrics',
  full_name='downlink_proto.SpaceComputerMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='power_voltage', full_name='downlink_proto.SpaceComputerMetrics.power_voltage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power_current', full_name='downlink_proto.SpaceComputerMetrics.power_current', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature_die', full_name='downlink_proto.SpaceComputerMetrics.temperature_die', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=779,
  serialized_end=872,
)


_SYSTEMMETRICS = _descriptor.Descriptor(
  name='SystemMetrics',
  full_name='downlink_proto.SystemMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='downlink_proto.SystemMetrics.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delayed', full_name='downlink_proto.SystemMetrics.delayed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power_supply', full_name='downlink_proto.SystemMetrics.power_supply', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='computer', full_name='downlink_proto.SystemMetrics.computer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imu', full_name='downlink_proto.SystemMetrics.imu', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digital', full_name='downlink_proto.SystemMetrics.digital', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='analog', full_name='downlink_proto.SystemMetrics.analog', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=875,
  serialized_end=1199,
)

_SYSTEMMETRICS.fields_by_name['time'].message_type = _TIMESTAMP
_SYSTEMMETRICS.fields_by_name['power_supply'].message_type = _POWERSUPPLYMETRICS
_SYSTEMMETRICS.fields_by_name['computer'].message_type = _SPACECOMPUTERMETRICS
_SYSTEMMETRICS.fields_by_name['imu'].message_type = _IMUMETRICS
_SYSTEMMETRICS.fields_by_name['digital'].message_type = _DIGITALMETRICS
_SYSTEMMETRICS.fields_by_name['analog'].message_type = _ANALOGMETRICS
DESCRIPTOR.message_types_by_name['DigitalMetrics'] = _DIGITALMETRICS
DESCRIPTOR.message_types_by_name['AnalogMetrics'] = _ANALOGMETRICS
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
DESCRIPTOR.message_types_by_name['PowerSupplyMetrics'] = _POWERSUPPLYMETRICS
DESCRIPTOR.message_types_by_name['IMUMetrics'] = _IMUMETRICS
DESCRIPTOR.message_types_by_name['SpaceComputerMetrics'] = _SPACECOMPUTERMETRICS
DESCRIPTOR.message_types_by_name['SystemMetrics'] = _SYSTEMMETRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DigitalMetrics = _reflection.GeneratedProtocolMessageType('DigitalMetrics', (_message.Message,), dict(
  DESCRIPTOR = _DIGITALMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.DigitalMetrics)
  ))
_sym_db.RegisterMessage(DigitalMetrics)

AnalogMetrics = _reflection.GeneratedProtocolMessageType('AnalogMetrics', (_message.Message,), dict(
  DESCRIPTOR = _ANALOGMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.AnalogMetrics)
  ))
_sym_db.RegisterMessage(AnalogMetrics)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMP,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.Timestamp)
  ))
_sym_db.RegisterMessage(Timestamp)

PowerSupplyMetrics = _reflection.GeneratedProtocolMessageType('PowerSupplyMetrics', (_message.Message,), dict(
  DESCRIPTOR = _POWERSUPPLYMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.PowerSupplyMetrics)
  ))
_sym_db.RegisterMessage(PowerSupplyMetrics)

IMUMetrics = _reflection.GeneratedProtocolMessageType('IMUMetrics', (_message.Message,), dict(
  DESCRIPTOR = _IMUMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.IMUMetrics)
  ))
_sym_db.RegisterMessage(IMUMetrics)

SpaceComputerMetrics = _reflection.GeneratedProtocolMessageType('SpaceComputerMetrics', (_message.Message,), dict(
  DESCRIPTOR = _SPACECOMPUTERMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.SpaceComputerMetrics)
  ))
_sym_db.RegisterMessage(SpaceComputerMetrics)

SystemMetrics = _reflection.GeneratedProtocolMessageType('SystemMetrics', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMMETRICS,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:downlink_proto.SystemMetrics)
  ))
_sym_db.RegisterMessage(SystemMetrics)


# @@protoc_insertion_point(module_scope)
