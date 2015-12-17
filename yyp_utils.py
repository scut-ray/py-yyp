#coding: utf8

__author__ = 'liangguanhui@qq.com'


import StringIO

def readfull(fd, size):
    total = None
    while True:
        buf = fd.read(size)
        if not buf:
            raise Exception("Can not readfull for size %s" % size)
        assert len(buf) <= size
        size -= len(buf)
        if size <= 0:
            if total is None:
                return buf
            else:
                total.write(buf)
                return total.getvalues()
        if total is None:
            total = StringIO()
        total.write(buf)
