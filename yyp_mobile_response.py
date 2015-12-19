#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_utils import readfull
import struct
from yyp_unmarshal import YYPUnMarshal

def ParseYYPMobileResponse(input):
    buf = readfull(input, 4)
    datasize = struct.unpack("I", buf)[0]
    if datasize < 38:
        raise YYPException("invalid data size: %s !" % datasize)
    data = readfull(input, datasize - 4)

    u = YYPUnMarshal(data)
    serviceUri = u.popUInt32()
    respCode = u.popUInt16()
    mobileAppId = u.popUInt32()
    mobileTopChannel = u.popUInt32()
    mobileSubChannel = u.popUInt32()
    uid = u.popUInt32()
    sendType = u.popUInt32()
    response = u.popString16()
    uids = u.popList(YYP_UINT32)

    u2 = YYPUnMarshal(response)
    mobileUri = u2.popUInt32()
    mobileExtendMap = u2.popDict(YYP_INT16, YYP_STRING16)
    response2 = u2.popString16()


    r = YYPMobileResponse(response2)

    r.serviceUri = serviceUri
    r.respCode = respCode
    r.mobileAppId = mobileAppId
    r.mobileTopChannel = mobileTopChannel
    r.mobileSubChannel = mobileSubChannel
    r.uid = uid
    r.sendType = sendType
    r.uids = uids

    r.mobileUri = mobileUri
    r.mobileExtendMap = mobileExtendMap

    return r

class YYPMobileResponse(YYPUnMarshal):
    pass

