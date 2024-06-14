from ctypes import LittleEndianStructure, c_char, c_uint8, c_uint16, sizeof
from abc import ABC, ABCMeta, abstractmethod

import sys
sys.path.append('../../')

from USBuzzer.enum.device_request import DescriptorType

class Descriptor(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
                    ('length', c_uint8),
                    ('descriptor_type', c_uint8),
                ]
    
    DESCRIPTOR_TYPE = DescriptorType.BASE

    def __init__(self):
        self.length          = sizeof(self)
        self.descriptor_type = self.DESCRIPTOR_TYPE

    def __str__(self):
        s = f'''Descriptor:\n'''

        # Due to specific inheritance behavior , _fields_ of subclass will not contains
        # _fields_ of the base class so we print them manually.
        s += f'''\tLength: {self.length}\n'''

        # Cast to DescriptorType the byte value contained in descriptor_type instance member
        # since we want to be sure that what is being printed is coming from the buffer itself
        # and not from instance's architecture, this would me misleading otherwise.
        s += f'''\tDescriptor type: {DescriptorType(self.descriptor_type).name}\n'''
            
        for f, t in self._fields_:
            s += f'''\t{f.capitalize().replace('_', ' ')}: {getattr(self, f)}\n'''
        
        return s

class ConfigurationDescriptor(Descriptor):
    """
    This class describes a configuration descriptor.
    """
    _fields_ = [
                    ("total_length", c_uint16),
                    ("num_interface", c_uint8),
                    ("configuration_value", c_uint8),
                    ("configuration_index", c_uint8),
                    ("attribute", c_uint8),
                    ("max_power", c_uint8),
                ]

    DESCRIPTOR_TYPE = DescriptorType.CONFIGURATION
    interface_list  = {}

    def add_interface(self, interface):
        """
        Adds an interface descriptor to the configuration.
        
        :param      interface:  The interface
        :type       interface:  InterfaceDescriptor
        """
        self.interface_list[interface.interface_number] = interface
        self.num_interface = len(self.interface_list)

class DeviceDescriptor(Descriptor):
    """
    This class describes a device descriptor.
    """
    _fields_ = [
                    ("USB", c_uint16),
                    ("device_class", c_uint8),
                    ("device_subclass", c_uint8),
                    ("device_protocol", c_uint8),
                    ("max_packet_size_0", c_uint8),
                    ("vendor_id", c_uint16),
                    ("product_id", c_uint16),
                    ("device_release", c_uint16),
                    ("index_manufacturer", c_uint8),
                    ("index_product", c_uint8),
                    ("index_serial_number", c_uint8),
                    ("num_configuration", c_uint8),
                ]

    DESCRIPTOR_TYPE = DescriptorType.DEVICE
    configuration_list = {}

    def add_configuration(self, configuration):
        """
        Adds a configuration to the device.
        
        :param      configuration:  The configuration
        :type       configuration:  ConfigurationDescriptor
        """
        self.configuration_list[configuration.configuration_value] = configuration
        self.num_configuration = len(self.configuration_list)

class DeviceQualifierDescriptor(Descriptor):
    _fields_ = [
                    ("USB", c_uint16),
                    ("device_class", c_uint8),
                    ("device_subclass", c_uint8),
                    ("device_protocol", c_uint8),
                    ("max_packet_size_0", c_uint8),
                    ("num_configuration", c_uint8),
                    ("reserved", c_uint8),
                ]

    DESCRIPTOR_TYPE = DescriptorType.QUALIFIER

    def __init__(self):
        self.reserved = 0

class EndpointDescriptor(Descriptor):
    """
    This class describes an endpoint descriptor.
    """
    _fields_ = [
                    ("endpoint_number", c_uint8, 4),
                    ("reserved", c_uint8, 3),
                    ("direction", c_uint8, 1),
                    ("attribute", c_uint8),
                    ("max_packet_size", c_uint16),
                    ("interval", c_uint8),
                ]

    DESCRIPTOR_TYPE = DescriptorType.ENDPOINT

class HIDDescriptor(Descriptor):
    pass

class InterfaceDescriptor(Descriptor):
    """
    This class describes an interface descriptor.
    """
    _pack_ = 1
    _fields_ = [
                    ("interface_number", c_uint8),
                    ("alternate_setting", c_uint8),
                    ("num_endpoint", c_uint8),
                    ("interface_class", c_uint8),
                    ("interface_subclass", c_uint8),
                    ("interface_protocol", c_uint8),
                    ("interface", c_uint8),
                ]
    
    DESCRIPTOR_TYPE = DescriptorType.INTERFACE
    endpoint_list = {}

    def add_endpoint(self, endpoint):
        """
        Adds an endpoint descriptor to the interface.
        
        :param      endpoint:  The endpoint
        :type       endpoint:  EndpointDescriptor
        """
        self.endpoint_list[endpoint.endpoint_number] = endpoint
        self.num_endpoint = len(self.endpoint_list)

class OtherSpeedDescriptor(Descriptor):
    _fields_ = [
                    ('total_length', c_uint16),
                    ('num_interface', c_uint8),
                    ('configuration_value', c_uint8),
                    ('configuration', c_uint8),
                    ('attribute', c_uint8),
                    ('max_power', c_uint8),
                ]

    DESCRIPTOR_TYPE = DescriptorType.OTHER_SPEED

class PhysicalDescriptor(Descriptor):
    _fields_ = []

class ReportDescriptor(Descriptor):
    pass

class StringDescriptor(Descriptor):
    """
    String descriptor are used for providing human readable information
    about the device.
    """
    _fields_ = [
                    # ("length", c_uint8),
                    # ("descriptor_type", c_uint8),
                    # ("data", c_uint16 * x),
                ]

    DESCRIPTOR_TYPE = DescriptorType.STRING

    def __init__(self, data = ''):
        super().__init__()
        self.data = data
        self.length = sizeof(Descriptor) + len(data)

    def __bytes__(self):
        class Payload(LittleEndianStructure):
            _pack_ = 1
            _fields_ = [
                            ("data", c_char * self.length),
                        ]
        
        payload = Payload()
        payload.data = self.data.encode('utf-16')

        return bytes(self) + bytes(payload)

    def __str__(self):
        '''
            The method is overriden since size is changing at runtime due
            to variable data size and so data is not straightly an instance's 
            member.
        '''
        s = super().__str__()
        s += f'''\tData: {self.data}\n'''
        
        return s
