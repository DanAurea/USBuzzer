from ctypes import LittleEndianStructure, c_uint8, c_uint16

import sys
sys.path.append('../../')

from USBuzzer.enum.device_request import DataTransferDirection, Type, Recipient, StandardRequestCode, StandardFeatureSelector
from USBuzzer.enum.packet_format import Token
from USBuzzer.protocol.packet import TokenPacket

class SetupPacket(TokenPacket):
    _pack_ = 1
    _fields_ =  [
                    ('recipient', c_uint8, 5),
                    ('type', c_uint8, 2),
                    ('data_transfer_direction', c_uint8, 1),
                    ('request', c_uint8),
                    ('value', c_uint16),
                    ('index', c_uint16),
                    ('length', c_uint16),
                ]

    PID      = Token.SETUP

    RECIPIENT               = Recipient.DEVICE
    TYPE                    = Type.STANDARD
    DATA_TRANSFER_DIRECTION = DataTransferDirection.HOST_DEVICE
    
    REQUEST                 = StandardRequestCode.DEFAULT
    DEFAULT_VALUE           = 0
    DEFAULT_INDEX           = 0
    DEFAULT_LENGTH          = 0

    def __init__(self, **args):
        super().__init__()
        self.recipient               = self.RECIPIENT
        self.type                    = self.TYPE
        self.data_transfer_direction = self.DATA_TRANSFER_DIRECTION
        self.request                 = self.REQUEST
        self.value                   = self.DEFAULT_VALUE
        self.index                   = self.DEFAULT_INDEX
        self.length                  = self.DEFAULT_LENGTH 

    def get_unspecified_packet(self):
        """
        This method serve as a generator for providing
        packet with format which are unspecified by USB
        specifications.
    
        This would be helpful for smart fuzzing approach.

        :returns:   Packet's instance.
        :rtype:     SetupPacket
        """
        return self

class ClearFeature(SetupPacket):
    REQUEST       = StandardRequestCode.CLEAR_FEATURE
    DEFAULT_VALUE = StandardFeatureSelector.ENDPOINT_HALT

class GetConfiguration(SetupPacket):
    REQUEST                 = StandardRequestCode.GET_CONFIGURATION
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST
    DEFAULT_LENGTH          = 1 

class GetDescriptor(SetupPacket):
    REQUEST                 = StandardRequestCode.GET_DESCRIPTOR
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST

class GetInterface(SetupPacket):
    REQUEST                 = StandardRequestCode.GET_INTERFACE
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST
    RECIPIENT               = Recipient.INTERFACE
    DEFAULT_LENGTH          = 1

class GetStatus(SetupPacket):
    REQUEST                 = StandardRequestCode.GET_INTERFACE
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST
    DEFAULT_LENGTH          = 2

class GetStatus(SetupPacket):
    REQUEST                 = StandardRequestCode.GET_INTERFACE
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST
    DEFAULT_LENGTH          = 2

class SetAddress(SetupPacket):
    REQUEST                 = StandardRequestCode.SET_ADDRESS

class SetConfiguration(SetupPacket):
    REQUEST                 = StandardRequestCode.SET_CONFIGURATION

class SetDescriptor(SetupPacket):
    REQUEST                 = StandardRequestCode.SET_DESCRIPTOR

class SetFeature(SetupPacket):
    REQUEST                 = StandardRequestCode.SET_FEATURE

class SetInterface(SetupPacket):
    REQUEST                 = StandardRequestCode.SET_INTERFACE
    RECIPIENT               = Recipient.INTERFACE

class SynchFrame(SetupPacket):
    REQUEST                 = StandardRequestCode.SYNCH_FRAME
    DATA_TRANSFER_DIRECTION = DataTransferDirection.DEVICE_HOST
    RECIPIENT               = Recipient.ENDPOINT
    DEFAULT_LENGTH          = 2