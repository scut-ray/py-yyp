#coding: utf8

__author__ = 'liangguanhui@qq.com'


import struct, StringIO
from __init__ import *
from yyp_utils import readfull

class YYPUnMarshal(object):

    def __init__(self, input):
        if isinstance(input, str):
            self._in = StringIO.StringIO(input)
        elif hasattr(input, 'read'):
            self._in = input
        else:
            raise Exception("not match input type!" + str(type(input)))

    def pop(self, type):
        if (type == YYP_INT8):
            buf = readfull(self._in, 1)
            return struct.unpack('b', buf)[0]
        elif (type == YYP_INT16):
            buf = readfull(self._in, 2)
            return struct.unpack('h', buf)[0]
        elif (type == YYP_INT32):
            buf = readfull(self._in, 4)
            return struct.unpack('i', buf)[0]
        elif (type == YYP_INT64):
            buf = readfull(self._in, 8)
            return struct.unpack('q', buf)[0]
        elif (type == YYP_UINT8):
            buf = readfull(self._in, 1)
            return struct.unpack('B', buf)[0]
        elif (type == YYP_UINT16):
            buf = readfull(self._in, 2)
            return struct.unpack('H', buf)[0]
        elif (type == YYP_UINT32):
            buf = readfull(self._in, 4)
            return struct.unpack('I', buf)[0]
        elif (type == YYP_UINT64):
            buf = readfull(self._in, 8)
            return struct.unpack('Q', buf)[0]
        elif (type == YYP_FLOAT32):
            buf = readfull(self._in, 4)
            return struct.unpack('f', buf)[0]
        elif (type == YYP_FLOAT64):
            buf = readfull(self._in, 8)
            return struct.unpack('d', buf)[0]
        elif (type == YYP_STRING16):
            buf = readfull(self._in, 2)
            l = struct.unpack('H', buf)[0]
            if l <= 0:
                return ""
            return readfull(self._in, l)
        elif (type == YYP_STRING32):
            buf = readfull(self._in, 4)
            l = struct.unpack('I', buf)[0]
            if l <= 0:
                return ""
            return readfull(self._in, l)

    def popInt8(self):
        return self.pop(YYP_INT8)

    def popInt16(self):
        return self.pop(YYP_INT16)

    def popInt32(self):
        return self.pop(YYP_INT32)

    def popInt64(self):
        return self.pop(YYP_INT64)

    def popUInt8(self):
        return self.pop(YYP_UINT8)

    def popUInt16(self):
        return self.pop(YYP_UINT16)

    def popUInt32(self):
        return self.pop(YYP_UINT32)

    def popUInt64(self):
        return self.pop(YYP_UINT64)

    def popFloat32(self):
        return self.pop(YYP_FLOAT32)

    def popFloat64(self):
        return self.pop(YYP_FLOAT64)

    def popString16(self):
        return self.pop(YYP_STRING16)

    def popString32(self):
        return self.pop(YYP_STRING32)

    def popList(self, type):
        l = self.popUInt32()
        ret = []
        for i in range(l):
            ret.append(self.pop(type))
        return ret

    def popStringList(self):
        return self.popList(YYP_STRING16)

    def popDict(self, keytype, valuetype):
        l = self.popUInt32()
        ret = {}
        for i in range(l):
            key = self.pop(keytype)
            value = self.pop(valuetype)
            ret[key] = value
        return ret

    def popStringDict(self):
        return self.popDict(YYP_STRING16, YYP_STRING16)
