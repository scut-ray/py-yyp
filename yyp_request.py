#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_response import ParseYYPResponse
from socket import socket

class YYPRequest(YYPMarshal):

    def __init__(self, uri, reqCode = 200):
        YYPMarshal.__init__(self)
        self.uri = uri
        self.reqCode = reqCode

    def sendAndWait(self, input):
        '''
        发送请求
        :param input: 可以是file类型，也可以是socket类型
        :return: YYPResponse
        '''
        data = self._buf.getvalue()
        l = len(data)
        m = YYPMarshal()
        m.putUInt32(l + 10)
        m.putUInt32(self.uri)
        m.putUInt16(self.reqCode)
        if isinstance(input, socket):
            input = input.makefile()
        m.write(input)
        self.write(input)
        input.flush()

        return ParseYYPResponse(input)


