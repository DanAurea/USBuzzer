from enum import IntEnum

class ClassCode(IntEnum):
    INTERFACE_DESCRIPTOR = 0x00
    AUDIO = 0x01
    COMMUNICATION_CDC_CONTROL = 0x02
    HID = 0x03
    PHYSICAL = 0x05
    IMAGE = 0x06
    PRINTER = 0x07
    MASS_STORAGE = 0x08
    HUB = 0x09
    CDC_DATA = 0x0A
    SMART_CARD = 0x0B
    CONTENT_SECURITY = 0x0D
    VIDEO = 0x0E
    PERSONAL_HEALTHCARE = 0x0F
    AUDIO_VIDEO = 0x10
    BILLBOARD = 0x11
    USB_TYPE_C_BRIDGE = 0x12
    USB_BULK_DISPLAY = 0x13
    MCTP = 0x14
    I3C = 0x3C
    DIAGNOSTIC = 0xDC
    WIRELESS_CONTROLLER = 0xE0
    MISCELLANEOUS = 0xEF
    APPLICATION_SPECIFIC = 0xFE
    VENDOR_SPECIFIC = 0xFF

class ImageCode(IntEnum):
    STILL_IMAGING = 0X01

class HUBCode(IntEnum):
    FULL_SPEED = 0x00
    HI_SPEED_SINGLE_TT = 0x01
    HI_SPEED_MULTI_TT = 0x02

class ContentSecurityCode(IntEnum):
    CONTENT_SECURITY = 0X00

class AudioVideoCode(IntEnum):
    AV_CONTROL = 0X00
    AV_DATA_VIDEO = 0X01
    AV_DATA_AUDIO = 0X02

class BillboardCode(IntEnum):
    BILLBOARD = 0X00

class USBTypeCBridgeCode(IntEnum):
    USB_TYPE_C_BRIDGE = 0X00

class USBBulkDisplayCode(IntEnum):
    USB_BDP = 0X00

class MCTPCode(IntEnum):
    MANAGEMENT_CONTROLLER = 0X00
    HOST = 0X01

class I3CCode(IntEnum):
    I3C = 0X00