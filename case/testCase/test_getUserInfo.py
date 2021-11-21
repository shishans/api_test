import os
import sys
import requests
import pytest
import urllib3
import allure
urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from case.func.getUserInfo import GetUserInfo

@allure.feature('web-用户-用户信息')
class TestGetUserInfo():

    @pytest.fixture(scope='class')
    def init(self,getHostAndProxies):
        host,proxies = getHostAndProxies
        return host,proxies

    @allure.story('传入正确的token，获取用户信息成功')
    def test_getUserInfo_sucess(self,getSession,init):
        '''传入正确的token，获取用户信息成功'''
        s = getSession
        host,proxies = init
        info = GetUserInfo(s,host)
        r = info.getUserInfo(proxies=proxies).json()
        assert r['code'] == '000000'
        assert r['data']['petName'] == '超级管理员'
        assert r['comment'] == 'Completed successfully'

    @allure.story('错误的token，获取用户信息失败')
    def test_getUserInfo_fail_01(self,init):
        '''错误的token，获取用户信息失败'''
        s = requests.session()
        host, proxies = init
        h = {
            'appid': '1514e1d61686438f95fa46f19070c126',
            'Authorization': '24661d2669614a3d8440a3f7208bdb6d'
        }
        s.headers.update(h)
        info = GetUserInfo(s, host)
        r = info.getUserInfo(proxies=proxies)
        assert r.status_code == 401

    @allure.story('token为空，获取用户信息失败')
    def test_getUserInfo_fail_02(self,init):
        '''token为空，获取用户信息失败'''
        host, proxies = init
        s = requests.session()
        h = {
            'appid': '1514e1d61686438f95fa46f19070c126',
            'Authorization': ''
        }
        s.headers.update(h)
        info = GetUserInfo(s, host)
        r = info.getUserInfo(proxies=proxies)
        assert r.status_code == 401



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