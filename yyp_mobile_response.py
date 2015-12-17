#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from yyp_utils import readfull
import struct
from yyp_unmarshal import YYPUnMarshal

def ParseYYPMobileResponse(input):
    buf = readfull(input, 4)
    datasize = struct.unpack("I", buf)
    if datasize < 38:
        raise YYPException("invalid data size: %s !" % datasize)
    data = readfull(input, datasize - 4)

    u = YYPUnMarshal(data)
    mobileUri = u.popUInt32()
    respCode = u.popUInt16()
    mobileAppId = u.popUInt32()
    mobileTopChannel = u.popUInt32()
    mobileSubChannel = u.popUInt32()
    uid = u.popUInt32()
    sendType = u.popUInt32()
    response = u.popString16()
    uids = u.popList(YYP_UINT32)

    r = YYPResponse(response)
    r.respCode = respCode
    r.mobileAppId = mobileAppId
    r.mobileTopChannel = mobileTopChannel
    r.mobileSubChannel = mobileSubChannel
    r.uid = uid
    r.sendType = sendType
    r.uids = uids

    return r

class YYPMobileResponse(YYPUnMarshal):
    pass

