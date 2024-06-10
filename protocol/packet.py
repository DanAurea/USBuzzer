from ctypes import LittleEndianStructure, c_char, c_uint8, c_uint16, sizeof

import sys
sys.path.append('../../')

from USBuzzer.enum.packet_format import PIDType, Token, Data, HandShake, Special

class Packet(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
                    ('pid_type', c_uint8, 2),
                    ('pid', c_uint8, 2),
                    ('pid_reserved', c_uint8, 4),
                ]

    PID_TYPE = PIDType.SPECIAL
    PID      = Special.RESERVED

    def __init__(self):
        self.pid_type = self.PID_TYPE
        self.pid      = self.PID

class TokenPacket(Packet):
    _fields_ = [
                    ('addr', c_uint16, 7),
                    ('endp', c_uint16, 4),
                    ('crc', c_uint16, 5),
                ]

    PID_TYPE = PIDType.TOKEN
    PID      = Token.OUT

class StartSplitTokenPacket(Packet):
    _fields_ = [
                    ('hub_addr', c_uint8, 7),
                    ('sc', c_uint8, 1),
                    ('port', c_uint8, 7),
                    ('s', c_uint8, 1),
                    ('e', c_uint8, 1),
                    ('et', c_uint8, 2),
                    ('crc5', c_uint8, 5),
                ]

    PID_TYPE = PIDType.SPECIAL
    PID      = Special.SPLIT

class CompleteSplitTokenPacket(Packet):
    _fields_ = [
                    ('hub_addr', c_uint8, 7),
                    ('sc', c_uint8, 1),
                    ('port', c_uint8, 7),
                    ('s', c_uint8, 1),
                    ('u', c_uint8, 1),
                    ('et', c_uint8, 2),
                    ('crc5', c_uint8, 5),
                ]

    PID_TYPE = PIDType.SPECIAL
    PID      = Special.SPLIT

class StartOfFramePacket(Packet):
    _fields_ = [
                    ('frame_number', c_uint16, 11),
                    ('crc5', c_uint16, 5),
                ]

    PID_TYPE = PIDType.TOKEN
    PID      = Token.SOF

class DataPacket(Packet):
    _fields_ = [
                    # TODO: Payload has to be defined at runtime (__bytes__ function has to be overriden)
                    #('data', x * c_uint8),
                    #('crc16', c_uin16),
                ]

    PID_TYPE = PIDType.DATA
    PID      = Data.DATA0

class HandShakePacket(Packet):
    PID_TYPE = PIDType.HANDSHAKE
    PID      = HandShake.ACK