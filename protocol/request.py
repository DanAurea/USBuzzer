from ctypes import LittleEndianStructure, c_uint8, c_uint16

class SetupData(LittleEndianStructure):
    _pack_ = 1
    _fields_ =  [
                    ('request_type', c_uint8),
                    ('request', c_uint8),
                    ('value', c_uint16),
                    ('index', c_uint16),
                    ('length', c_uint16),
                ]