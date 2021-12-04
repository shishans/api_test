import os
import sys
import requests
import pytest
import allure
import urllib3
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from case.func.classificationDelete import ClassificationDelete
from case.func.classificationAdd import ClassificationAdd
from common.tools import timestamp

@allure.feature('web-分类-删除分类')
class TestClassificationDelete():

    @pytest.fixture(scope='module')
    def start_up(self,getSession,getHostAndProxies):
        s = getSession
        host,proxies = getHostAndProxies
        add = ClassificationAdd(s, host)
        dele = ClassificationDelete(s,host)
        add = ClassificationAdd(s,host)
        return add,dele,add,proxies

    @allure.story('删除存在的分类id，删除成功')
    def test_classificationDelete_sucess(self,start_up):
        #先新增一个分类
        add, dele, add, proxies = start_up
        name = str(timestamp(16))
        data = {
            'name': name,
            'parentId': '0',
            'status': 'DEFAULT',
            'source': 'APPX',
            'proxies': proxies
        }
        r = add.classificationAdd(**data)
        classificationId = r['data']
        r = dele.classificationDelete(classificationId,proxies)
        assert r['code'] == '000000'

    @allure.story('删除不存在的分类id，删除失败')
    @allure.issue('https://ums.dreawer.com/#/login?type=login')
    @pytest.mark.parametrize('classificationId',['1234akjfdjhgfieuur'])
    def test_classificationDelete_fail(self,start_up,classificationId):
        add, dele, add, proxies = start_up
        classificationId = classificationId
        r = dele.classificationDelete(classificationId, proxies)
        assert r['comment'] == '不允许操作数据'
        assert r['code'] == '112030'

    @allure.story('检查必填项分类id为空')
    @allure.testcase('https://www.baidu.com/')
    @pytest.mark.parametrize('classificationId',[''])
    def test_classificationDelete_sucess(self,start_up,classificationId):
        add, dele, add, proxies = start_up
        classificationId = classificationId
        r = dele.classificationDelete(classificationId, proxies)
        assert r['comment'] == '输入检查错误'
        assert r['code'] == '113000'


