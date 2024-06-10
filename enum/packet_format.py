from enum import IntEnum

class PIDType(IntEnum):
    TOKEN     = 0b01
    DATA      = 0b11
    HANDSHAKE = 0b10
    SPECIAL   = 0b00

class Token(IntEnum):
    OUT   = 0b00
    IN    = 0b10
    SOF   = 0b01
    SETUP = 0b11

class Data(IntEnum):
    DATA0 = 0b00
    DATA1 = 0b10
    DATA2 = 0b01
    MDATA = 0b11

class HandShake(IntEnum):
    ACK   = 0b00
    NAK   = 0b10
    STALL = 0b11
    NYET  = 0b01

class Special(IntEnum):
    PRE      = 0b11
    ERR      = 0b11
    SPLIT    = 0b10
    PING     = 0b01
    RESERVED = 0b00