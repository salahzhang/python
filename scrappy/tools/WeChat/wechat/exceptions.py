# -*- coding: utf-8 -*-

class WechatException(Exception):
    """基于搜狗搜索的的微信公众号爬虫接口  异常基类
    """
    pass


class WechatVcodeException(WechatException):
    """基于搜狗搜索的的微信公众号爬虫接口 出现验证码 异常类
    """
    pass


class WechatRequestsException(WechatException):
    """基于搜狗搜索的的微信公众号爬虫接口 抓取 异常类
    """
    def __init__(self, errmsg, status_code):
        WechatException(errmsg)
        self.status_code = status_code