from enum import IntEnum

class DataTransferDirection(IntEnum):
    """
    Data transfer direction is assigned as bit 7 in bmRequestType
    """
    HOST_DEVICE = 0X00
    DEVICE_HOST = 0X01

class Type(IntEnum):
    """
    Type is assigned as bit 5-6 in bmRequestType
    """
    STANDARD = 0X00
    CLASS    = 0X01
    VENDOR   = 0X02
    RESERVED = 0X03

class Recipient(IntEnum):
    """
    Recipient is assigned as bit 0-4 in bmRequestType
    """
    DEVICE    = 0X00
    INTERFACE = 0X01
    ENDPOINT  = 0X02
    OTHER     = 0X03
    RESERVED  = 0X04
    # TODO add values upto 1F as reserved

class StandardRequestCode(IntEnum):
    GET_STATUS        = 0X00
    CLEAR_FEATURE     = 0X01
    RESERVED          = 0X02
    SET_FEATURE       = 0X03
    RESERVED2         = 0X04
    SET_ADDRESS       = 0X05
    GET_DESCRIPTOR    = 0X06
    SET_DESCRIPTOR    = 0X07
    GET_CONFIGURATION = 0X08
    SET_CONFIGURATION = 0X09
    GET_INTERFACE     = 0X0A
    SET_INTERFACE     = 0X0B
    SYNCH_FRAME       = 0X0C
    DEFAULT           = 0XFF

class DescriptorType(IntEnum):
    BASE          = 0X00
    DEVICE        = 0X01
    CONFIGURATION = 0X02
    STRING        = 0X03
    INTERFACE     = 0X04
    ENDPOINT      = 0X05
    QUALIFIER     = 0X06
    OTHER_SPEED   = 0X07
    INTERFACE_POWER = 0X08

class StandardFeatureSelector(IntEnum):
    ENDPOINT_HALT        = 0X00
    DEVICE_REMOTE_WAKEUP = 0X01
    TEST_MODE            = 0X02