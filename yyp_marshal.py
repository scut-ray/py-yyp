#coding: utf8

__author__ = 'liangguanhui@qq.com'


import struct, StringIO
from __init__ import *

class YYPMarshal(object):

    def __init__(self):
        self._buf = StringIO.StringIO()

    def write(self, output):
        output.write(self._buf.getvalue())

    def put(self, type, v):
        if (type == YYP_INT8):
            self._buf.write(struct.pack('b', v))
        elif (type == YYP_INT16):
            self._buf.write(struct.pack('h', v))
        elif (type == YYP_INT32):
            self._buf.write(struct.pack('i', v))
        elif (type == YYP_INT64):
            self._buf.write(struct.pack('q', v))
        elif (type == YYP_UINT8):
            self._buf.write(struct.pack('B', v))
        elif (type == YYP_UINT16):
            self._buf.write(struct.pack('H', v))
        elif (type == YYP_UINT32):
            self._buf.write(struct.pack('I', v))
        elif (type == YYP_UINT64):
            self._buf.write(struct.pack('Q', v))
        elif (type == YYP_FLOAT32):
            self._buf.write(struct.pack('f', v))
        elif (type == YYP_FLOAT64):
            self._buf.write(struct.pack('d', v))
        elif (type == YYP_STRING16):
            assert isinstance(v, str)
            l = len(v)
            self._buf.write(struct.pack('H', l))
            self._buf.write(v)
        elif (type == YYP_STRING32):
            assert isinstance(v, str)
            l = len(v)
            self._buf.write(struct.pack('I', l))
            self._buf.write(v)
        else:
            raise YYPException("Invalid type %s" % type)

    def putInt8(self, number):
        self.put(YYP_INT8, number)

    def putInt16(self, number):
        self.put(YYP_INT16, number)

    def putInt32(self, number):
        self.put(YYP_INT32, number)

    def putInt64(self, number):
        self.put(YYP_INT64, number)

    def putUInt8(self, number):
        self.put(YYP_UINT8, number)

    def putUInt16(self, number):
        self.put(YYP_UINT16, number)

    def putUInt32(self, number):
        self.put(YYP_UINT32, number)

    def putUInt64(self, number):
        self.put(YYP_UINT64, number)

    def putFloat32(self, f):
        self.put(YYP_FLOAT32, f)

    def putFloat64(self, f):
        self.put(YYP_FLOAT64, f)

    def putString16(self, s):
        self.put(YYP_STRING16, s)

    def putString32(self, s):
        self.put(YYP_STRING32, s)

    def putList(self, type, lst):
        if lst is None:
            self.putUInt32(0)
            return
        if not isinstance(lst, list) and not isinstance(lst, tuple):
            raise YYPException("Invalid list type %s" % type(lst))
        l = len(lst)
        self.putUInt32(l)
        for v in lst:
            self.put(type, v)

    def putDict(self, keytype, valuetype, d):
        if d is None:
            self.putUInt32(0)
            return
        if not isinstance(d, dict):
            raise YYPException("Invalid dict type %s" % type(d))
        l = len(d)
        self.putUInt32(l)
        for k, v in d.items():
            self.put(keytype, k)
            self.put(valuetype, v)

    def putEmptyStringList(self):
        #self.putDict(YYP_STRING16, YYP_STRING16, {})
        self.putUInt32(0)

    def putEmptyStringDict(self):
        #self.putList(YYP_STRING16, ())
        self.putUInt32(0)
