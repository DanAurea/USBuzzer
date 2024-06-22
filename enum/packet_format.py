from enum import IntEnum

class Token(IntEnum):
    OUT   = 0b0001
    IN    = 0b1001
    SOF   = 0b0101
    SETUP = 0b1101

class Data(IntEnum):
    DATA0 = 0b0011
    DATA1 = 0b1011
    DATA2 = 0b0111
    MDATA = 0b1111

class HandShake(IntEnum):
    ACK   = 0b0010
    NAK   = 0b1010
    STALL = 0b1110
    NYET  = 0b0110

class Special(IntEnum):
    PRE      = 0b1100
    ERR      = 0b1100
    SPLIT    = 0b1000
    PING     = 0b0100
    RESERVED = 0b0000