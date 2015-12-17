#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_mobile_response import ParseYYPMobileResponse
from StringIO import StringIO
import struct
from yyp_utils import str2intip

class YYPMobileRequest(YYPMarshal):

    def __init__(self, uri, reqCode = 200):
        YYPMarshal.__init__(self)
        self.uri = uri
        self.reqCode = reqCode
        self.mobileExtendMap = {
            1 : "0",
            2 : "2",
            3 : "9610fa75c5f3fd30f525ac7e5e44f3184cc79847",
            5 : "^_324",
            6 : "4.4.0",
        }
        self.uid = 0
        self.mobileTopChannel = 0
        self.mobileSubChannel = 0
        self.mobileServerId = 0
        self.mobileClientType = 2
        self.mobileUserIp = 0
        self.mobileServiceProxyIp = 0
        self.mobileAppId = 60035
        self.mobileExtendInfo = {}
        self.mobileExtendInfo2 = {}

    def setMobileExtendMap(self, mExtMap):
        self.mobileExtendMap = mExtMap

    def setUid(self, uid):
        self.uid = uid

    def setMobileTopChannel(self, c):
        self.mobileTopChannel = c

    def setMobileSubChannel(self, c):
        self.mobileSubChannel = c

    def setMobileServerId(self, serverId):
        self.mobileServerId = serverId

    def setMobileClientType(self, clientType):
        self.mobileClientType = clientType

    def setMobileUserIp(self, userIp):
        if isinstance(userIp, str):
            ret, ip = str2intip(userIp)
            if not ret:
                raise YYPException("Invalid ip str %s" % userIp)
            userIp = ip
        self.mobileUserIp = userIp

    def setMobileServiceProxyIp(self, proxyIp):
        if isinstance(proxyIp, str):
            ret, ip = str2intip(proxyIp)
            if not ret:
                raise YYPException("Invalid ip str %s" % proxyIp)
            proxyIp = ip
        self.mobileServiceProxyIp = proxyIp

    def setMobileAppId(self, appId):
        self.mobileAppId = appId

    def setMobileExtendInfo(self, extendInfo):
        self.mobileExtendInfo = extendInfo

    def setMobileExtendInfo2(self, extendInfo):
        self.mobileExtendInfo2 = extendInfo

    def sendAndWait(self, sock):
        m = YYPMarshal()
        m.putUInt32(208 + 1 * 256)  # mobile service的uri,固定值
        m.putUInt16(self.reqCode)
        m.putUInt32(self.uri)
        m.putDict(YYP_INT16, YYP_STRING16, self.mobileExtendMap)

        s = StringIO()
        self.write(s)
        data = s.getvalue()
        m.putString16(data)

        m.putUInt32(self.uid)
        m.putUInt32(self.mobileTopChannel)
        m.putUInt32(self.mobileSubChannel)
        m.putUInt32(self.mobileServerId)
        m.putUInt32(self.mobileClientType)
        m.putUInt32(self.mobileUserIp)
        m.putUInt32(self.mobileServiceProxyIp)
        m.putUInt32(self.mobileAppId)

        m.putEmptyStringDict() #extendInfo, TODO
        m.putEmptyStringDict() #extendInfo2, TODO

        s = StringIO()
        m.write(s)
        data = s.getvalue()

        ll = len(data) + 4

        ld = struct.pack('I', ll)

        sock.send(ld)
        sock.send(data)

        return ParseYYPMobileResponse(sock.makefile())
