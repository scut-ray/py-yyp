#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_response import ParseYYPResponse

class YYPRequest(YYPMarshal):

    def __init__(self, uri, reqCode = 200):
        YYPMarshal.__init__(self)
        self.uri = uri
        self.reqCode = reqCode

    def sendAndWait(self, sock):
        data = self._buf.getvalue()
        l = len(data)
        m = YYPMarshal()
        m.putUInt32(l + 10)
        m.putUInt32(self.uri)
        m.putUInt16(self.reqCode)
        sockfile = sock.makefile()
        m.write(sockfile)
        self.write(sockfile)
        sockfile.flush()

        return ParseYYPResponse(sockfile)


