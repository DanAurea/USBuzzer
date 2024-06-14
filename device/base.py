import sys
sys.path.append('../../')

from USBuzzer.enum import DeviceSpeed, LanguageID
from USBuzzer.enum.device_class import ClassCode
from USBuzzer.protocol.descriptor import DeviceDescriptor, ConfigurationDescriptor
from USBuzzer.utils import decimal_to_bcd

class USBBaseDevice(object):
    device_class    = ClassCode.PHYSICAL
    device_subclass = 0
    device_protocol = 0

    device_release    = 1.0
    usb_version       = 2.0

    product_id        = 0x0000
    vendor_id         = 0x0000
    max_packet_size   = 64

    manufacturer  = "USBuzzer"
    product       = "Generic USB device"
    serial_number = "01234"

    speed = DeviceSpeed.FULL

    language_list = (LanguageID.ENGLISH_US, )

    def __init__(self):
        self._device_descriptor = DeviceDescriptor()
        
        self._device_descriptor.USB                 = decimal_to_bcd(self.usb_version)
        
        self._device_descriptor.device_class        = self.device_class
        self._device_descriptor.device_subclass     = self.device_subclass
        self._device_descriptor.device_protocol     = 0

        self._device_descriptor.max_packet_size_0   = self.max_packet_size
        
        self._device_descriptor.vendor_id           = self.vendor_id
        self._device_descriptor.product_id          = self.product_id
        self._device_descriptor.device_release      = decimal_to_bcd(self.device_release)
        
        self._device_descriptor.index_manufacturer  = 0
        self._device_descriptor.index_product       = 0
        self._device_descriptor.index_serial_number = 0
        
        self._device_descriptor.num_configuration   = 0

    def add_configuration(self, configuration):
        """
        Adds a configuration descriptor to the device.
        
        :param      configuration:  The configuration
        :type       configuration:  ConfigurationDescriptor
        """
        self._device_descriptor.add_configuration(configuration)

class GenericHIDDevice(USBBaseDevice):
    device_class = ClassCode.HID

class GenericCDCDevice(USBBaseDevice):
    device_class = ClassCode.CDC_DATA

class GenericADCDevice(USBBaseDevice):
    pass

class GenericMassStorageDevice(USBBaseDevice):
    device_class = ClassCode.MASS_STORAGE