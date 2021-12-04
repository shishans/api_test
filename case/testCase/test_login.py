import sys
import os
import requests
import pytest
import allure

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.func.login import Login

@allure.feature('web-登录')
class TestLogin():
    s = requests.session()

    @allure.story('不存在的账号登录')
    @pytest.mark.parametrize('phoneNumber,password',[('15972939790','hbc23687')])
    def test_login_01(self,phoneNumber,password,getHostAndProxies):
        '''不存在的用户登录'''
        host,proxies = getHostAndProxies
        l = Login(self.s,host)
        r = l.login(phoneNumber=phoneNumber,password=password,proxies=proxies)
        assert r['comment'] == '数据不存在'
        assert r['data'] == None

    @allure.story('正确的账号，错误的密码')
    @pytest.mark.parametrize('phoneNumber,password',[('15527060286','hbc236871')])
    def test_login_02(self,phoneNumber,password,getHostAndProxies):
        '''存在的用户名错误的密码进行登录'''
        host, proxies = getHostAndProxies
        l = Login(self.s,host)
        r = l.login(phoneNumber=phoneNumber,password=password,proxies=proxies)
        assert r['comment'] == '业务检查错误'
        assert r['data'] == None

    @allure.story('检查必填项，手机号或密码为空')
    @pytest.mark.parametrize('phoneNumber,password,exp',
                             [('','hbc23687','ecmps.phoneNumber'),
                              ('15527060286','','ecmps.password')])
    def test_login_03(self,phoneNumber,password,exp,getHostAndProxies):
        '''用户名为空,密码为空'''
        host, proxies = getHostAndProxies
        l = Login(self.s,host)
        r = l.login(phoneNumber=phoneNumber,password=password,proxies=proxies)
        assert r['checkPoint'] == exp
        assert r['comment'] == '输入检查错误'











