#对requests请求进行二次封装处理
import logging
import requests

from api.user.index import LOGINPATH
from conf.globaldata import BASEURL
from logging import config

config.fileConfig('./conf/log.conf')
# 获取打印日志对象
logger = logging.getLogger()
# logger.info("普通日志");
# logger.error("错误日志")



def req(url,session=requests,method="GET",params=None,data=None,json=None,files=None,headers=None):
    try:
        res = session.request(method=method,url=f'{BASEURL}{url}',params=params,data=data,json=json,files=files,headers=headers)
    except Exception as result:
        logger.error(f'接口名称{url},请求方式{method},参数{params or data or json or files},请求头{headers},报错信息{result}')
    else:
        http_status_code = res.status_code
        if res.status_code == 200:
            return {
                "headers": res.headers,
                "data": res.json()
            }
        elif res.status_code == 401:
            logger.debug(f' [401] 接口名称{url},请求方式{method},参数{params or data or json or files},请求头{headers},报错信息401,接口的实际结果{res.text}')
            return False
        elif res.status_code == 404:
            logger.debug(
                f' [404] 接口名称{url},报错信息404,接口路径错误')
            return False
        elif res.status_code == 405:
            logger.debug(
                f' [405] 接口名称{url},请求方式{method},参数{params or data or json or files},请求头{headers},报错信息405,请求方式错误')
            return False
        elif res.status_code == 400:
            logger.debug(
                f' [400] 接口名称{url},请求方式{method},参数{params or data or json or files},报错信息400,接口请求参数错误')
            return False
        elif res.status_code == 500:
            logger.error(f' [500] 接口名称{url},请求方式{method},参数{params or data or json or files},请求头{headers},报错信息500,接口服务器异常\n{res.text}')
            return False
        elif res.status_code == 502:
            logger.error(f'[502] 接口路径{url},报错信息502,服务器代理异常')
            return False
        elif res.status_code == 504:
            logger.error(f'[504] 接口路径{url},报错信息504,接口超时')
            return False
        else:
            return False


if __name__ == '__main__':
    res = req(url = LOGINPATH,method="GET",params="post",json = {
        "account":"18888888888",
        "password":"admin123",
        "client":2
    })
    print(res)




