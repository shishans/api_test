import os
import sys
import requests
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.mylogger import logger

class GetUserInfo():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/bsmc/user/getInfo'

    @allure.step('获取用户信息')
    def getUserInfo(self,proxies=None):
        r = self.s.get(url=self.url,verify=False,proxies=proxies)
        logger.info('getUserToken接口运行时间：%f' % (r.elapsed.total_seconds()))
        return r


if __name__ == '__main__':
    from case.getSession import getSession
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    s = getSession(host=host,proxies=proxies)
    info = GetUserInfo(s,host)
    r = info.getUserInfo(proxies=proxies)
    print(r)