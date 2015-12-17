#coding: utf8

__author__ = 'liangguanhui@qq.com'

from __init__ import *
from StringIO import StringIO
from socket import socket
import sys

EntproxyHost = None
EntproxyPort = None


def as_hex(b):
    ret = []
    t = []
    for c in b:
        t.append("%03d" % ord(c))
        if len(t) >= 16:
            ret.append(" ".join(t))
            t = []
    if t:
        ret.append(" ".join(t))
    return "\n".join(ret)

def test_yyp_marshal_1():
    out = StringIO()
    m = YYPMarshal()
    m.putInt8(-2**7)
    m.putUInt8(2**8-1)
    m.putInt16(2**15 - 1)
    m.putUInt16(2**16 - 1)
    m.putInt32(-5)
    m.putUInt32(2**32 - 1)
    m.putInt64(-2**63)
    m.putUInt64(1000)

    s16 = "hello world,nimen"
    s32 = "yyp test sdk"
    m.putString16(s16)
    m.putString32(s32)

    lst = ["you", "are", "the", "best"]
    map = {"age": 20, "height": 127}
    m.putList(YYP_STRING16, lst)
    m.putDict(YYP_STRING16, YYP_INT8, map)

    m.write(out)

    data = out.getvalue()
    print as_hex(data)

    u = YYPUnMarshal(data)
    assert u.popInt8() == -2**7
    assert u.popUInt8() == 2**8 - 1
    assert u.popInt16() == 2**15 - 1
    assert u.popUInt16() == 2**16 - 1
    assert u.popInt32() == -5
    assert u.popUInt32() == 2**32 - 1
    assert u.popInt64() == -2**63
    assert u.popUInt64() == 1000

    assert u.popString16() == s16
    assert u.popString32() == s32

    assert u.popList(YYP_STRING16) == lst
    assert u.popDict(YYP_STRING16, YYP_INT8) == map

def test_yyp_marshal():
    test_yyp_marshal_1()

def test_yyp_request_1():
    req = YYPRequest(213 + 100 * 256)
    residParam = 1129004823438361330
    req.putInt64(residParam)
    req.putEmptyStringDict()

    sock = socket()
    sock.connect((EntproxyHost, EntproxyPort))
    resp = req.sendAndWait(sock)

    assert resp.uri == 213 + 101 * 256
    assert resp.respCode == 200

    code = resp.popUInt32()
    resid = resp.popUInt64()
    prop = resp.popStringDict()

    assert code == 0
    assert resid == residParam
    assert isinstance(prop, dict)
    assert prop

    print "code =", code
    print "resid =", resid
    for k, v in prop.items():
        print "%15s => %s" % (k, v)



def test_yyp_request():
    test_yyp_request_1()

def main():
    global EntproxyHost, EntproxyPort
    EntproxyHost = sys.argv[1]
    EntproxyPort = int(sys.argv[2])

    test_yyp_marshal()
    test_yyp_request()

if __name__ == "__main__":
    # 使用方法： python yyp_test.py <EntProxyHost> <EntProxyPort>
    main()
