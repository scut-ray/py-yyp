#coding: utf8

__author__ = 'liangguanhui@qq.com'


YYP_STRING16 = 100
YYP_STRING32 = 101

YYP_INT8 = 200
YYP_INT16 = 201
YYP_INT32 = 202
YYP_INT64 = 203

YYP_UINT8 = 300
YYP_UINT16 = 301
YYP_UINT32 = 302
YYP_UINT64 = 303

YYP_FLOAT32 = 400
YYP_FLOAT64 = 401


from yyp_marshal import  YYPMarshal
from yyp_unmarshal import YYPUnMarshal
from yyp_request import YYPRequest
from yyp_response import YYPResponse
from yyp_mobile_request import YYPMobileRequest
from yyp_mobile_response import YYPMobileResponse
from yyp_exception import YYPException