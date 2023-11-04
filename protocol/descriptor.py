from ctypes import LittleEndianStructure, c_char, c_uint8, c_uint16

class ConfigurationDescriptor(LittleEndianStructure):
    """
    This class describes a configuration descriptor.
    """
    _pack_ = 1
    _fields_ = [
                    ("length", c_uint8),
                    ("descriptor_type", c_uint8),
                    ("total_length", c_uint16),
                    ("num_interface", c_uint8),
                    ("configuration_value", c_uint8),
                    ("configuration_index", c_uint8),
                    ("attribute", c_uint8),
                    ("max_power", c_uint8),
                ]

    def __str__(self):
        s = (f"Length: {self.length}\n"
             f"Descriptor type: {self.descriptor_type}\n"
             f"Total length: {self.total_length}\n"
             f"Number of interfaces: {self.num_interface}\n"
             f"Configuration value: {self.configuration_value}\n"
             f"Configuration index: {self.configuration_index}\n"
             f"Attribute: {self.attribute}\n"
             f"Max power: {self.max_power}\n"
            )
        return s

class DeviceDescriptor(LittleEndianStructure):
    """
    This class describes a device descriptor.
    """
    _pack_ = 1
    _fields_ = [
                    ("length", c_uint8),
                    ("descriptor_type", c_uint8),
                    ("USB", c_uint16),
                    ("device_class", c_uint8),
                    ("device_subclass", c_uint8),
                    ("device_protocol", c_uint8),
                    ("max_packet_size_0", c_uint8),
                    ("vendor_id", c_uint16),
                    ("product_id", c_uint16),
                    ("device", c_uint16),
                    ("manufacturer", c_uint8),
                    ("product", c_uint8),
                    ("serial_number", c_uint8),
                    ("num_configuration", c_uint8),
                ]
    
    def __str__(self):
        s = (f"Length: {self.length}\n"
             f"Descriptor type: {self.descriptor_type}\n"
             f"USB specification: {self.USB}\n"
             f"Device class: {self.device_class}\n"
             f"Device subclass: {self.device_subclass}\n"
             f"Device protocol: {self.device_protocol}\n"
             f"Max packet size endpoint 0: {self.max_packet_size}\n"
             f"Vendor ID (VID): {self.vendor_id}\n"
             f"Product ID (PID): {self.product_id}\n"
             f"Device: {self.device}\n"
             f"Manufacturer: {self.manufacturer}\n"
             f"Product: {self.product}\n"
             f"Serial number: {self.serial_number}\n"
             f"Number of configuration: {self.num_configuration}\n"
            )
        return s

class EndpointDescriptor(LittleEndianStructure):
    """
    This class describes an endpoint descriptor.
    """
    _pack_ = 1
    _fields_ = [
                    ("length", c_uint8),
                    ("descriptor_type", c_uint8),
                    ("endpoint_address", c_uint8),
                    ("attribute", c_uint8),
                    ("max_packet_size", c_uint16),
                    ("interval", c_uint8),
                ]

    def __str__(self):
        s = (f"Length: {self.length}\n"
             f"Descriptor type: {self.descriptor_type}\n"
             f"Endpoint address: {self.endpoint_address}\n"
             f"Attribute: {self.attribute}\n"
             f"Max packet size: {self.max_packet_size}\n"
             f"Interval: {self.interval}\n"
            )
        return s

class HIDDescriptor(LittleEndianStructure):
    pass

class InterfaceDescriptor(LittleEndianStructure):
    """
    This class describes an interface descriptor.
    """
    _pack_ = 1
    _fields_ = [
                    ("length", c_uint8),
                    ("descriptor_type", c_uint8),
                    ("interface_number", c_uint8),
                    ("alternate_setting", c_uint8),
                    ("num_endpoint", c_uint8),
                    ("interface_class", c_uint8),
                    ("interface_subclass", c_uint8),
                    ("interface_protocol", c_uint8),
                    ("interface", c_uint8),
                ]

    def __str__(self):
        s = (f"Length: {self.length}\n"
             f"Descriptor type: {self.descriptor_type}\n"
             f"Interface number: {self.interface_number}\n"
             f"Alternate setting: {self.alternate_setting}\n"
             f"Number of endpoint: {self.num_endpoint}\n"
             f"Interface class: {self.interface_class}\n"
             f"Interface subclass: {self.interface_subclass}\n"
             f"Interface protocol: {self.interface_protocol}\n"
             f"Interface: {self.interface}\n"
            )
        return s

class PhysicalDescriptor(LittleEndianStructure):
    _pack_ = 1
    _fields_ = []

class ReportDescriptor(LittleEndianStructure):
    pass

class StringDescriptor(LittleEndianStructure):
    """
    String descriptor are used for providing human readable information
    about the device.
    """
    _pack_ = 1
    _fields_ = [
                    # ("length", c_uint8),
                    # ("descriptor_type", c_uint8),
                    # ("data", c_uint16 * x),
                ]

    def __init__(self):
        self.length          = 0
        self.descriptor_type = 0
        self.data            = ''

    def __bytes__(self):
        class Payload(LittleEndianStructure):
            _pack_ = 1
            _fields_ = [
                            ("length", c_uint8),
                            ("descriptor_type", c_uint8),
                            ("data", c_char * self.length),
                        ]
        
        payload = Payload()
        payload.length          = self.length
        payload.descriptor_type = self.descriptor_type
        payload.data            = self.data.encode('utf-16')

        return bytes(payload)

    def __str__(self):
        s = (f"Length: {self.length}\n"
             f"Descriptor type: {self.descriptor_type}\n"
             f"Data: {self.data}\n"
            )
        return s