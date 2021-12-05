import os
import sys
import pytest
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.mylogger import logger
from case.func.classificationUpdateStatus import ClassificationUpdateStatus
from case.func.classificationAdd import ClassificationAdd

# @allure.story('web-分类-更新分类')
# class TestClassificationUpdateStatus():
#
#     @pytest.fixture(scope='module')
#     def start_up(self,getSession,getHostAndProxies):
#         s = getSession
#         host,proxies = getHostAndProxies
#         add = ClassificationAdd(s,host)
#         update = ClassificationUpdateStatus(s,host)
#         return proxies,add,update
#
#     @allure.story('禁用的分类改为正常')
#     def test_ClassificationUpdateStatus(self,start_up):
#         proxies,add,update = start_up
#         #先add一个禁用状态的分类
#         data = {
#
#         }
#         r = add.classificationAdd(**data)
#         class_id = r['data']
#         # 将禁用的改为正常
#         update.classificationUpdateStatus()
#         # 获取分类列表，遍历遍历，找到这个分类id，检查status
#         # 数据库查询，检查status字段
#
#
#     @allure.story('')
#     def test_ClassificationUpdateStatus_01(self,start_up):
#         proxies,add,update = start_up
#         #先add一个禁用状态的分类
#         data = {
#
#         }
#         r = add.classificationAdd(**data)
#         class_id = r['data']
#         # 将禁用的改为正常
#         update.classificationUpdateStatus()
#         # 获取分类列表，遍历遍历，找到这个分类id，检查status
#         # 数据库查询，检查status字段

