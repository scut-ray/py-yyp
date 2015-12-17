# py-yyp

py-yyp是一款对yy协议(YY Protocol)进行编码解码的python第三方库.目前支持简单的bio请求.

使用方法如下(以调用YY娱乐的神曲接口信息为例)

<pre>
    req = YYPRequest(213 + 100 * 256)
    req.putInt64(1129004823438361330)
    req.putEmptyStringDict()

    sock = socket()
    sock.connect((EntproxyHost, EntproxyPort))
    resp = req.sendAndWait(sock)

    code = resp.popUInt32()
    resid = resp.popUInt64()
    prop = resp.popStringDict()

    print "code =", code
    print "resid =", resid
    for k, v in prop.items():
        print "%15s => %s" % (k, v)
</pre>
