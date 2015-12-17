#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_utils import readfull
import struct
from yyp_unmarshal import YYPUnMarshal

def ParseYYPResponse(input):
    buf = readfull(input, 10)
    datasize, uri, respCode = struct.unpack("IIH", buf)
    data = readfull(input, datasize - 10)
    return YYPResponse(datasize, uri, respCode, data)

class YYPResponse(YYPUnMarshal):

    def __init__(self, datasize, uri, respCode, input):
        YYPUnMarshal.__init__(self, input)
        self.datasize = datasize
        self.uri = uri
        self.respCode = respCode
